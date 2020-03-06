import hashlib
passwd = '0e84c7a330fd4e52ba2616a25ba2dc83'
password = input("What is your passwd?: ")
hashed = hashlib.md5(password.encode())
if hashed == passwd:
    print ("okay")
