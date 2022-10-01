from hashlib import sha256

text = "Secure Transaction"
hash_result = sha256(text.encode())
print(hash_result.hexdigest())
