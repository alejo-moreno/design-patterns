from abc import ABCMeta

#Component
class Shape (metaclass=ABCMeta):
    def draw(self): 
        pass
    
#ConcreteComponent    
class Circle(Shape):
    def draw(self): 
        print ("I am a Circle")
        
class Rectangle(Shape):
    def draw(self): 
        print ("I am a Rectangle")
        
 #Decorator       
class ShapeDecorator(Shape):
    def __init__(self,decoratedShape):
        self.decoratedShape = decoratedShape
        
    def draw(self):
        self.decoratedShape.draw()
        
    def doSomethingElse(self): 
        pass     
        
#ConcreteDecorator        
class ColorRedShapeDecorator(ShapeDecorator):
            def draw(self):
                self.decoratedShape.draw()
                self.doSomethingElse()
        
            def doSomethingElse(self):
                print("Coloring red")
                
                
if __name__ == "__main__":
    circle = Circle()
    redCircle = ColorRedShapeDecorator(Circle())
    
    circle.draw()
    print("#########")
    redCircle.draw()

