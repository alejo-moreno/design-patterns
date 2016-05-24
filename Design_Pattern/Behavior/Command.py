from abc import ABCMeta

#Command
class Command(metaclass=ABCMeta):
    def execute(self):
        pass
        
#Receiver
class Light:
    def turnOn(self):
        print("Foco encendido")
        
    def turnOff(self):
        print("Foco apagado")        
        
#Invoker
class Switch:
    def __init__(self,onCommand,offCommand):
        self._onCommand = onCommand
        self._offCommand = offCommand
        
    def on(self):
        self._onCommand.execute()       
        
    def off(self):
        self._offCommand.execute()
        
#ConcreteCommand        
class onCommand(Command):
    def __init__(self,light):
        self._light = light
        
    def execute(self):
        self._light.turnOn()               
        
class offCommand(Command):
    def __init__(self,light):
        self._light = light
        
    def execute(self):
        self._light.turnOff()
        
#Client
class LightSwitch:
    def __init__(self):
        self._bulb = Light()
        self._switchUp = onCommand(self._bulb)
        self._switchDown = offCommand(self._bulb)
        self._switch = Switch(self._switchUp,self._switchDown)
            
    def operation(self,cmd):
        if cmd == "ON":
           self._switch.on()
        elif cmd == "OFF":
           self._switch.off()
        else:
            print("Invalid Operation")
           
if __name__ == "__main__":
     client = LightSwitch()
     print("Testing ON command")
     client.operation("ON")
     print("Testing OFF command")
     client.operation("OFF")