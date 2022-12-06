from Crypto.Cipher import AES
from secrets import *
from DES import *

key = token_bytes(16)
print()
print(key)
print()

mykey=55375033928667909896388332047712080889262454158108340124726201483053206332764

encrypt_ECC("mykey",mykey)

def encrypt(msg):
    cipher = AES.new(key, AES.MODE_EAX)
    nonce = cipher.nonce
    ciphertext, tag = cipher.encrypt_and_digest(msg.encode('ascii'))
    return nonce, ciphertext, tag

def decrypt(nonce, ciphertext, tag):
    cipher = AES.new(key, AES.MODE_EAX, nonce=nonce)
    plaintext = cipher.decrypt(ciphertext)
    try:
        cipher.verify(tag)
        return plaintext.decode('ascii')
    except:
        return False

nonce, ciphertext, tag = encrypt("text to encrypt")
plaintext = decrypt(nonce, ciphertext, tag)
print(f'Cipher text: {ciphertext}')
if not plaintext:
    print('Message is corrupted')
else:
    print(f'Plain text: {plaintext}')


# print(randbelow(112312431254125))
# randbits = mykey.getrandbits
# print(randbits)

token_hex(mykey)