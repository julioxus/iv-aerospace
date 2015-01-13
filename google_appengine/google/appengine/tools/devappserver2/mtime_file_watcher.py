#!/usr/bin/env python
#
# Copyright 2007 Google Inc.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
#
"""Monitors a directory tree for changes using mtime polling."""

import os
import threading
import warnings

from google.appengine.tools.devappserver2 import watcher_common


class MtimeFileWatcher(object):
  """Monitors a directory tree for changes using mtime polling."""

  # TODO: evaluate whether we can directly support multiple directories.
  SUPPORTS_MULTIPLE_DIRECTORIES = False

  def __init__(self, directory):
    self._directory = directory
    self._quit_event = threading.Event()
    self._filename_to_mtime = None
    self._changes = set()
    self._changes_lock = threading.Lock()
    self._watcher_thread = threading.Thread(target=self._watch_changes)
    self._watcher_thread.daemon = True

  def start(self):
    """Start watching a directory for changes."""
    self._watcher_thread.start()

  def quit(self):
    """Stop watching a directory for changes."""
    self._quit_event.set()

  def changes(self):
    """Returns the set of changed paths since the last call.

    start() must be called before this method.

    Returns:
      Returns the set of file paths changes if the watched directory has changed
      since the last call to changes or, if has_changes has never been called,
      since start was called.
    """
    with self._changes_lock:
      changes = self._changes
      self._changes = set()
      return changes

  def _watch_changes(self):
    while not self._quit_event.wait(1):
      self._check_for_changes()

  def _check_for_changes(self):
    new_changes = self._changed_paths()
    if new_changes:
      with self._changes_lock:
        self._changes |= new_changes

  def _changed_paths(self):
    """Returns the paths changed since last call."""
    self._filename_to_mtime, old_filename_to_mtime = (
        self._generate_filename_to_mtime(), self._filename_to_mtime)

    # Emulates the original "ignore the first round" behavior.
    if old_filename_to_mtime is None:
      return set()

    diff_items = set(self._filename_to_mtime.items()).symmetric_difference(
        old_filename_to_mtime.items())
    return {filename for filename, _ in diff_items}

  def _generate_filename_to_mtime(self):
    filename_to_mtime = {}
    num_files = 0
    for dirname, dirnames, filenames in os.walk(self._directory,
                                                followlinks=True):
      watcher_common.skip_ignored_dirs(dirnames)
      filenames = [f for f in filenames if not watcher_common.ignore_file(f)]
      for filename in filenames + dirnames:
        if num_files == 10000:
          warnings.warn(
              'There are too many files in your application for '
              'changes in all of them to be monitored. You may have to '
              'restart the development server to see some changes to your '
              'files.')
          return filename_to_mtime
        num_files += 1
        path = os.path.join(dirname, filename)
        try:
          mtime = os.path.getmtime(path)
        except (IOError, OSError):
          pass
        else:
          filename_to_mtime[path] = mtime
    return filename_to_mtime
