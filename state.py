class Machine():
    state = None
    lightstate = None
    brightness = 0

    def __init__(self):
        self.state = CalcOffClass()
        self.lightstate = LightOffClass()
    
    def calcOn(self):
        self.state.calcOn(self)
    
    def calcOff(self):
        self.state.calcOff(self)

    def setBrightness(self,brightness):
        if isinstance(self.state,CalcOffClass):
            print('kalkulator mati, tidak bisa menyalakan lampu!')
        else: 
            self.brightness = brightness

    def lightOn(self):
        if  isinstance(self.state,CalcOffClass):
            print('kalkulator mati, tidak bisa menyalakan lampu!')
        else:
            self.lightstate.lightOn(self)
    
    def lightOff(self):
        if  isinstance(self.state,CalcOffClass):
            print('kalkulator mati, tidak bisa menyalakan lampu!')
        else:
            self.lightstate.lightOff(self)

class CalcOnClass():
    def calcOn(self,machine):
        print("kalkulator sudah aktif")
    def calcOff(self,machine):
        machine.brightness = 0
        machine.state = CalcOffClass()
        print("Kalkulator Beralih ke Mode OFF")

class CalcOffClass():
    def calcOn(self,machine):
        machine.state = CalcOnClass()
        machine.brightness = 10
        machine.lightstate = LightOnClass()
        print("Kalkulator Beralih ke mode ON")
    def calcOff(self,machine):
        print("kalkulator sudah mati")

class LightOnClass():
    def lightOn(self,machine):
        print("Lampu sudah menyala")
    def lightOff(self,machine):
        machine.brightness=0
        machine.lightstate = LightOffClass()
        print("mematikan lampu")

class LightOffClass():
    def lightOn(self,machine):
        machine.brightness=10
        machine.lightstate = LightOnClass()
        print("menyalakan lampu")
    def lightOff(self,machine):
        print("Lampu sudah menyala")

if __name__=='__main__':
    
    #initialize state
    machine=Machine()

    machine.calcOn()
    print(machine.brightness)  
    machine.lightOff()
    print(machine.brightness)
    machine.lightOn()
    machine.setBrightness(8)
    print(machine.brightness)
    machine.calcOff()
    print(machine.brightness)
    machine.setBrightness(8)