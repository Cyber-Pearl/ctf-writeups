from Crypto.Cipher import AES
from Crypto.Util.Padding import unpad
import hashlib

with open("flag.enc", "rb") as f:
    encrypted_data = f.read()

iv = encrypted_data[:AES.block_size]
ciphertext = encrypted_data[AES.block_size:]

# Key (must be the same key used for encryption)

# https://github.com/Lukerd-29-00/unbreakable/commit/8ceff412507d2122c28a09a5ad13b92e6dab96b5
key = hashlib.sha256(b"tasciewapeoiu").digest() # makita ra ang key sa commit log HAHAHAHHA "removed password from repo"

cipher = AES.new(key, AES.MODE_CBC, iv)
decrypted_data = unpad(cipher.decrypt(ciphertext), AES.block_size)
decrypted_text = decrypted_data.decode('utf-8')

print("Decrypted Flag:", decrypted_text)



