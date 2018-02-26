import os
import validators


package_directory = os.path.dirname(os.path.abspath(__file__))

MODULE_EXTENSIONS = ('.py', '.pyc', '.pyo')


def newKeyStore(file):
    #validate valid path
    print("generating key store")


    #private key stored in path outside

## Functions to build
#-ListKeys(keystore)
#-UpdateKey(name)
#-NewKeyStore()
#-DeleteKeyStore(keystore)
#-MigrateKeystore(oldkeystore, newkeystore) 
    #You cannont change keys on a keystore.
    #You must create a new keystore move the keys
    #then, delete the old keystore and keys,
    # after validating the keys were moved properly.

    #public key stored in keys folder for encrypting secrets. 

def addKey(name, secret):
    """Creates a new key to store API credentials.""" 
    ## New Feature ##
    #add optional urlbase parameter
    #use requests to valdate baseurl (200) response 
    #Check for existing keystore

    #Validate Input
    if name == "":
        raise ValueError("'name' must not be blank.")
    
    if secret == "":
        raise ValueError("'secret' must not be blank.")

    if name == None:
        raise ValueError("'name' cannot be blank")
   
    if type(name) != str:
          raise ValueError("'name' must be str")
    else:
        testname = name + ".py"
    
    if type(secret) != str:
        raise ValueError("'secret' must be str")    
    
    if "init" in name:
        errorMsg = "Must use module name " + name + " is not a valid name"
        raise ValueError(errorMsg)

    if "pycache" in name:
        errorMsg = "Must use module name " + name + " is not a valid name"
        raise ValueError(errorMsg)

    if testname not in set(os.listdir(package_directory)):
        raise ValueError("Must use module name")

    
    #Look for existing public key

    return secret
    

#print(add(name="slack", secret="secret"))  




