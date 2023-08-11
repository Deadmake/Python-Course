import random
import string


sizei = int(input("How long should you password be? "))
charachters = "!§$%&/()=?#+'*_-" 

if type(number):
    def pwgen (size):
        pas="".join(
            random.choice(charachters + string.ascii_uppercase + string.ascii_lowercase + string.digits)
            for _ in range(size)) 
        return pas
else:
    print("ERROR")
    

print (pwgen(sizei)),
