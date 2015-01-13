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
"""A handler that displays logs for instances."""

from google.appengine.api import request_info
from google.appengine.tools.devappserver2.admin import admin_request_handler


class LogsHandler(admin_request_handler.AdminRequestHandler):
  _DEFAULT_SHOW_LINES = 30

  def get(self):
    params = self.request.params
    if 'module_name' in params:
      module_name = params['module_name']
    else:
      self.abort(404, detail='module_name should be defined.')
      return

    try:
      module = self.dispatcher.get_module_by_name(module_name)
    except request_info.ModuleDoesNotExistError:
      self.abort(404, detail=('There is no such module with name \'%s\'.' %
                              (module_name)))
      return

    if 'instance_id' in params:
      instance_id = params['instance_id']
    else:
      self.abort(404, detail='instance_id should be defined.')
      return

    try:
      instance = module.get_instance(instance_id)
    except request_info.InvalidInstanceIdError:
      self.abort(404, detail=('There is no such instance with instance_id'
                              '%s\'.' % (instance_id)))
      return

    log_file_names = instance.get_log_file_names()
    if 'log_file_name' in params:
      log_file_name = params['log_file_name']
      if log_file_name not in log_file_names:
        self.abort(404, detail=('There is no such log file.'))
        return

      if 'show_lines' in params:
        show_lines = int(params['show_lines'])
      else:
        self.abort(404, detail=(
            'Number of requested lines should be specified.'))
        return

      count_lines = instance.get_logs_size(log_file_name)
      show_lines = max(0, min(show_lines, count_lines))
      logs_data = instance.get_logs(log_file_name, show_lines)
    else:
      log_file_name = None
      logs_data = []
      show_lines = 0
      count_lines = 0

    values = {'module': module, 'instance': instance, 'logs_data': logs_data,
              'log_file_name': log_file_name, 'log_file_names': log_file_names,
              'show_lines': show_lines, 'count_lines': count_lines,
              'default_show_lines': self._DEFAULT_SHOW_LINES}
    self.response.write(self.render('instance_logs.html', values))
