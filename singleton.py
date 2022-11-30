class SingletonObject:
    _singletonObject = None
 
    @staticmethod
    def getSingletonObjectInstance():
        if SingletonObject._singletonObject is None:
            SingletonObject._singletonObject = SingletonObject()

        return SingletonObject._singletonObject

    def getMessage(self):
        print ("Halo... Selamat datang di ITK")
        

from SingletonObject import SingletonObject

singletonObject = SingletonObject.getSingletonObjectInstance()

singletonObject.getMessage()