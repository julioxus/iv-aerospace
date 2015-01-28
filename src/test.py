import unittest
from google.appengine.ext import db
from google.appengine.ext import testbed
from google.appengine.datastore import datastore_stub_util
from server import Tests

class aerospaceTestCase(unittest.TestCase):
	

	def setUp(self):
		# First, create an instance of the Testbed class.
		self.testbed = testbed.Testbed()
		# Then activate the testbed, which prepares the service stubs for use.
		self.testbed.activate()
		# Initialize the datastore stub with this policy.
		self.testbed.init_datastore_v3_stub()

	def tearDown(self):
		self.testbed.deactivate()
		
	def test(self):
		pruebas = Tests()
		
		response = pruebas.testInicial(2)
		self.assertEqual(response,4)
		
		response = pruebas.testURL()
		self.assertEqual(response, True)
	
		response = pruebas.testBD()
		self.assertEqual(response,True)
		
			

if __name__ == '__main__':
    unittest.main()