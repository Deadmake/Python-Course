import random
import string


sizei = int(input("How long should you password be? "))
charachters = "!§$%&/()=?#+'*_-" 

def pwgen (sizei):
    pas="".join(
        random.choice(charachters + string.ascii_uppercase + string.ascii_lowercase + string.digits)
         for _ in range(sizei)) 
    return pas
   
print (pwgen(sizei)),
