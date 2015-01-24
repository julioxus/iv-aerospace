import unittest
from google.appengine.ext import db
from google.appengine.ext import testbed
from google.appengine.datastore import datastore_stub_util
from server import Tests
from google.appengine.ext.webapp.util import run_wsgi_app

class aerospaceTestCase(unittest.TestCase):
	

	def setUp(self):
		# First, create an instance of the Testbed class.
		self.testbed = testbed.Testbed()
		# Then activate the testbed, which prepares the service stubs for use.
		self.testbed.activate()
		# Create a consistency policy that will simulate the High Replication consistency model.
		self.policy = datastore_stub_util.PseudoRandomHRConsistencyPolicy(probability=0)
		# Initialize the datastore stub with this policy.
		self.testbed.init_datastore_v3_stub(consistency_policy=self.policy)

	def tearDown(self):
		self.testbed.deactivate()
		
	def test(self):
		pruebas = Tests()
		#response = pruebas.testBD()
		response = pruebas.testInicial(webapp2.RequestHandler,2)
		self.assertEqual(response,4)

if __name__ == '__main__':
    unittest.main()