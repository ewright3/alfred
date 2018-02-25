import os


package_directory = os.path.dirname(os.path.abspath(__file__))

MODULE_EXTENSIONS = ('.py', '.pyc', '.pyo')


def newKeyStore(file):
    #validate valid path
    print("generating key store")


    #private key stored in path outside


    #public key stored in keys folder for encrypting secrets. 

def addKey(name, secret):
    
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