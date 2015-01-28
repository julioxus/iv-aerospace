import unittest
from google.appengine.ext import db
from google.appengine.ext import testbed
from google.appengine.datastore import datastore_stub_util
from server import Tests


class TestModel(db.Model):
  """A model class used for testing."""
  number = db.IntegerProperty(default=42)
  text = db.StringProperty()

class TestEntityGroupRoot(db.Model):
  """Entity group root"""
  pass

def GetEntityViaMemcache(entity_key):
  """Get entity from memcache if available, from datastore if not."""
  entity = memcache.get(entity_key)
  if entity is not None:
    return entity
  entity = TestModel.get(entity_key)
  if entity is not None:
    memcache.set(entity_key, entity)
  return entity

class aerospaceTestCase(unittest.TestCase):
	

	def setUp(self):
		# First, create an instance of the Testbed class.
		self.testbed = testbed.Testbed()
		# Then activate the testbed, which prepares the service stubs for use.
		self.testbed.activate()
		# Initialize the datastore stub with this policy.
		self.testbed.init_datastore_v3_stub()
		self.testbed.init_memcache_stub()

	def tearDown(self):
		self.testbed.deactivate()
		
	def test(self):
		pruebas = Tests()
		
		#Probamos el test inicial
		response = pruebas.testInicial(2)
		self.assertEqual(response,4)
		
		#Probamos que las url esten funcionando
		response = pruebas.testURL()
		self.assertEqual(response, True)
		
		#Probamos que la página web esté activa y no esté caida
		response = pruebas.testPaginaActiva()
		self.assertEqual(response,True)
		
	# Probamos a insertar en la base de datos
	def testInsertEntity(self):
		TestModel().put()
		response = 1
		self.assertEqual(response, len(TestModel.all().fetch(2)))
		

if __name__ == '__main__':
    unittest.main()
