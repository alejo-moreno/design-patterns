from abc import ABCMeta, abstractmethod

class Car (metaclass=ABCMeta):
    def __init__(self):
       self.name = None
       self.maxSpeed = None
    
    def __str__(self):
        return "name is {}, maxSpeed is {}".format(self.name,self.maxSpeed)
        
        
class SportsCar(Car):
    def __init__(self):
       self.name = "Deportivo"
       self.maxSpeed = "250 km/h"
        
class FamilyCar(Car):
    def __init__(self):
       self.name = "Familiar"
       self.maxSpeed = "150 km/h"
       
class AbstractFactory(metaclass=ABCMeta):
    def __init__(self):        
       self.manufacturer = None       
    
    def __str__(self):
        return "manufacturer is {}".format(self.manufacturer)    
    
    @abstractmethod
    def createCar(self,carType): pass
    
    @staticmethod
    def get_factory(factoryName):
        if factoryName == "Audi":
            return AudiFactory()
        elif factoryName == "BMW":
            return BMWFactory()    
        raise TypeError("Unknown Factory")
       
class AudiFactory(AbstractFactory):
    def __init__(self):        
       self.manufacturer = "Audi"

    def createCar(self,carType):
        self.car = None
        if carType == "sports":
            self.car = SportsCar();
        elif carType == "family":
            self.car = FamilyCar();
        else:
            print("Car type {} is not defined".format(carType))    
        return self.car
        
    def doSomething(self):
        print(self.car)       
        
class BMWFactory(AbstractFactory):
    def __init__(self):        
       self.manufacturer = "BMW"

    def createCar(self,carType):
        self.car = None
        if carType == "sports":
            self.car = SportsCar();
        elif carType == "family":
            self.car = FamilyCar();
        else:
            print("Car type {} is not defined".format(carType))    
        return self.car
        
    def doSomething(self):
        print(self.car) 
            
if __name__ == "__main__":
        myAbstractFactory = AbstractFactory.get_factory("Audi")
        print(myAbstractFactory)
        s = myAbstractFactory.createCar("sports")
        f = myAbstractFactory.createCar("family")
                
        print(s)
        print(f)  
        
        myAbstractFactory = AbstractFactory.get_factory("BMW")
        print(myAbstractFactory) 
        s= myAbstractFactory.createCar("sports")
        f = myAbstractFactory.createCar("family")
                 
        print(s)
        print(f)  
      
        
        