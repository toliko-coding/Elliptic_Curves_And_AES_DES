import EccCore
class Server:
    # privet_key
    # public_key
    # shared_key

    def __init__(self,private):
        self.private_key = private
        
    
    def GeneratePublicKey(self,Gx,Gy,a,b,mod):
        self.Public_X, self.Public_Y = EccCore.applyDoubleAndAddMethod(Gx, Gy, self.private_key, a, b, mod)
        print("Server Public x :" , self.Public_X ,"\n" , "Server Public y :" , self.Public_Y)


    def GenerateSharedKey(self,ClientPubKey_X,ClientPubKey_Y,a,b,mod):
        self.Shared_X, self.Shared_Y = EccCore.applyDoubleAndAddMethod(ClientPubKey_X, ClientPubKey_Y, self.private_key, a, b, mod)
        print("Server Shared x :" , self.Shared_X ,"\n" ,"Server Shared y :" , self.Shared_Y)
