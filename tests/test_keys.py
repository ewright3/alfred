import unittest
from ..casey.modules import keys



#Test Key Creation

class TestKeys(unittest.TestCase):
    def test_addKey_name_values(self):
        #Raise ValueError if Key name does not match module name
        self.assertRaises(ValueError,keys.addKey,name="UnknowModule", secret="a secret")

        #Raise ValueError if key name equal internal module
        self.assertRaises(ValueError,keys.addKey,name="__init__", secret="a secret")
        self.assertRaises(ValueError,keys.addKey,name="__pycache__", secret="a secret")
        self.assertRaises(ValueError,keys.addKey,name="__doc__", secret = "a secret.")
        
        #Raises ValueError if full module name is not used
        self.assertRaises(ValueError,keys.addKey,name="down", secret="a secret")
        self.assertRaises(ValueError,keys.addKey,name="d", secret="a secret")
        
        #Raise ValueError if key name is None or Blank
        self.assertRaises(ValueError, keys.addKey, name=None, secret="secret")
        self.assertRaises(ValueError, keys.addKey, name="", secret="secret")
        
        #Raise ValueError if key name is a boolean
        self.assertRaises(ValueError, keys.addKey, name=True, secret="secret")
        self.assertRaises(ValueError, keys.addKey, name=False, secret="secret")
        
    def test_addKey_secret_values(self):
        #Raise ValueError if key secret is None or Blank
        self.assertRaises(ValueError, keys.addKey, name="downloader", secret=None)
        self.assertRaises(ValueError, keys.addKey, name="downloader", secret="")

        #Raise ValueError if key secret is a boolean
        self.assertRaises(ValueError,keys.addKey, name="downloader", secret=True)
        self.assertRaises(ValueError,keys.addKey, name="downloader", secret=False)           
    
    def test_addKey_output(self):
        #if module is in name then secret should equal secret
        self.assertEqual(keys.addKey(name="slack", secret="secret"),"secret")


   
   
#Test Key Storage




# Test Key Retrieve


