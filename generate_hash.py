import hashlib

pswd = "1q2w3e4r5t6y"
hash = hashlib.sha256(pswd.encode('utf-8'))

print(hash.hexdigest())