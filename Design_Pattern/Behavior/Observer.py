from abc import ABCMeta, abstractmethod

#Observer Interface
class Publisher(metaclass=ABCMeta):
    def __init__(self):
        pass
        
    def addObserver(self,observer):
        pass
    
    def removeObserver(self,observer):
        pass        
    
    def notifyAll(self):
        pass
        
class PlatziForum (Publisher):
    def __init__(self):
        self.userList = []
        self.post = None
                
    def addObserver(self,observer):
        if observer not in self.userList:
            self.userList.append(observer)
    
    def removeObserver(self,observer):
        if observer in self.userList:
            self.userList.remove(observer)
    
    def notifyAll(self):
        for observer in self.userList:
            observer.notify(self.post)        
        
    def writePost(self,text):
        self.post = text
        self.notifyAll()    
        
        
class Subscriber:
    def __init__(self):
        pass
        
    def notify(self,post):
        pass
        
class UserA(Subscriber):
    def __init__(self):
        pass
        
    def notify(self,post):
        print('UserA has been notified {}'.format(post))
        
class UserB(Subscriber):
    def __init__(self):
        pass
        
    def notify(self,post):
        print('UserB has been notified {}'.format(post))        
        
if __name__ == "__main__":
     foroPlatzi = PlatziForum()
     userA = UserA()
     userB = UserB()
     
     foroPlatzi.addObserver(userA)
     foroPlatzi.addObserver(userB)
     
     foroPlatzi.writePost("My first post on forum")
     
     foroPlatzi.removeObserver(userB);
     
     foroPlatzi.writePost("My second post on forum")