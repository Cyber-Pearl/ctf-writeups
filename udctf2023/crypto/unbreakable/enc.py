import hashlib
from Crypto.Cipher import AES
from Crypto.Util.Padding import pad
import os
key = os.urandom(16)

with open("flag.txt","r") as f:
    flag = f.read().strip().encode()

iv = os.urandom(AES.block_size)

ct = AES.new(key,AES.MODE_CBC,iv).encrypt(pad(flag,AES.block_size))

with open("flag.enc","wb") as f:
    f.write(iv + ct)
