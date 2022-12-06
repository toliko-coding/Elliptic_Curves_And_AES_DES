import EccCore
class Client:
    # privet_key
    # public_key
    # shared_key

    def __init__(self,private):
        self.private_key = private
    
    def getPrivateKey(self):
        return self.prvate_key
        

    def GeneratePublicKey(self,Gx,Gy,a,b,mod):
        self.Public_X, self.Public_Y = EccCore.applyDoubleAndAddMethod(Gx, Gy, self.private_key, a, b, mod)
        print("Client Public x :" , self.Public_X ,"\n" ,"Client Public y :" , self.Public_Y)


    def GenerateSharedKey(self,ServerPubKey_X,ServerPubKey_Y,a,b,mod):
        self.Shared_X, self.Shared_Y = EccCore.applyDoubleAndAddMethod(ServerPubKey_X, ServerPubKey_Y, self.private_key, a, b, mod)
        print("Client Shared x :" , self.Shared_X ,"\n", "Client Shared y :" , self.Shared_Y)
