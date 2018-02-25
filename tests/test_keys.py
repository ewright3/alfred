import unittest
from ..casey.modules import keys



#Test Key Creation

class TestKeys(unittest.TestCase):
    def test_add_key_values(self):

        #Raise ValueError if Key name does not match module name
        self.assertRaises(ValueError,keys.add,name="UnknowModule", secret="a secret")

        #Raise ValueError if key name equal internal module
        self.assertRaises(ValueError,keys.add,name="__init__", secret="a secret")
        self.assertRaises(ValueError,keys.add,name="__pycache__", secret="a secret")
        
        #Raises ValueError if full module name is not used
        self.assertRaises(ValueError,keys.add,name="sla", secret="a secret")
        self.assertRaises(ValueError,keys.add,name="d", secret="a secret")
        
        #if module is in name then secret should equal secret
        self.assertEqual(keys.add(name="slack", secret="secret"),"secret")
        
        #Raise ValueError if key name is None
        self.assertRaises(ValueError, name = None, secret="secret")
        #Raise ValueError if key name is a boolean

        #Raise ValueError if key secret is None

        #Raise ValueError if key secret is a boolean


   
   
#Test Key Storage




# Test Key Retrieve


