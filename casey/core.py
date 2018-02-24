
def read_instruction(message):
    if message == None:
        raise ValueError("The message cannot be empty.")
    
    if message == False:
        raise ValueError("The message can not be set to False.")
    message = message
    return message