import os

package_directory = os.path.dirname(os.path.abspath(__file__))

MODULE_EXTENSIONS = ('.py', '.pyc', '.pyo')

def add(name, secret):
    
    #Validate Input
    testname = name + ".py"

    if "init" in name:
        errorMsg = "Must use module name " + name + " is not a valid name"
        raise ValueError(errorMsg)

    if "pycache" in name:
        errorMsg = "Must use module name " + name + " is not a valid name"
        raise ValueError(errorMsg)

    if testname not in set(os.listdir(package_directory)):
        raise ValueError("Must use module name")
    
    if name == None:
        raise ValueError("'Name' cannot be blank")

    #Look for existing public key

    

    return secret
    
    
         