import re

def fun(s):
    if re.search("^[\w-]+@[a-zA-Z0-9]+\.[a-zA-Z]{1,3}$", s):
        return True
    else: 
        return False
    

            
