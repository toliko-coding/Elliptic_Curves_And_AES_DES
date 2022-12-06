from Client import *
from Server import *
import random

from Crypto.Cipher import AES
from Crypto.Random import get_random_bytes


Client_RandomKey = random.getrandbits(128)
print("Random key : " , Client_RandomKey)

Server_RandomKey = random.getrandbits(128)
print("Random key : " , Server_RandomKey)

mod = pow(2, 256) - pow(2, 32) - pow(2, 9) - pow(2, 8) - pow(2, 7) - pow(2, 6) - pow(2, 4) - pow(2, 0)
order = random.getrandbits(128)
#curve configuration
# y^2 = x^3 + a*x + b = y^2 = x^3 + 7
a = 2
b = 2

#base point on the curve - G
Gx = random.getrandbits(128)
Gy = random.getrandbits(128)

print("---------------------")
print("initial configuration")
print("---------------------")
print("Curve: y^2 = x^3 + ",a,"*x + ",b, " mod ", mod," , #F(",mod,") = ", order)
print("Base point: (",Gx,", ",Gy,")")
print("modulo: ", mod)
print("order of group: ", order)



print("\n------------------------------------------")
print("Elliptic Curve Diffie Hellman Key Exchange")
print("------------------------------------------")


C = Client(Client_RandomKey)
C.GeneratePublicKey(Gx,Gy,a,b,mod)

S = Server(Server_RandomKey)
S.GeneratePublicKey(Gx,Gy,a,b,mod)

print()
print("Shared Key : \n")
C.GenerateSharedKey(S.Public_X,S.Public_Y,a,b,mod)
S.GenerateSharedKey(C.Public_X,C.Public_Y,a,b,mod)





# data = b'secret data'

# key = get_random_bytes(16)
# cipher = AES.new(key, AES.MODE_EAX)
# ciphertext, tag = cipher.encrypt_and_digest(data)
# nonce = cipher.nonce

# cipher = AES.new(key, AES.MODE_EAX, nonce)
# data = cipher.decrypt_and_verify(ciphertext, tag)

