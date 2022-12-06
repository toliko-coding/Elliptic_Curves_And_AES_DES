from Client import *
from Server import *
import random
from tinyec import registry
import DES
import hashlib, secrets, binascii


from Crypto.Cipher import *
from Crypto.Random import get_random_bytes
from secrets import token_bytes



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

curve = registry.get_curve('brainpoolP256r1')


# msg = b'Text to be encrypted by ECC public key and ' \
#       b'decrypted by its corresponding ECC private key'
# print("original msg:", msg)
# privKey = secrets.randbelow(curve.field.n)
# print("PPPPPPPPP" ,privKey)
# pubKey = privKey * curve.g
# print("PPPPPPPPP" ,pubKey)


# encryptedMsg = DES.encrypt_ECC(msg, pubKey)
# encryptedMsgObj = {
#     'ciphertext': binascii.hexlify(encryptedMsg[0]),
#     'nonce': binascii.hexlify(encryptedMsg[1]),
#     'authTag': binascii.hexlify(encryptedMsg[2]),
#     'ciphertextPubKey': hex(encryptedMsg[3].x) + hex(encryptedMsg[3].y % 2)[2:]
# }
# print("encrypted msg:", encryptedMsgObj)

# decryptedMsg = DES.decrypt_ECC(encryptedMsg, privKey)
# print("decrypted msg:", decryptedMsg)