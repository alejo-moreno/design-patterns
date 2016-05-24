from abc import ABCMeta, abstractmethod

class TextFinder(metaclass=ABCMeta):
    def find(self,text):
        pass
        
class SpanishFinder(TextFinder):
    def find(self,text):
        return " {} fue encontrado".format(text)
        
class EnglishFinder(TextFinder):
    def find(self,text):
        return " {} was found".format(text)
        
if __name__ == "__main__":
    finderOne = SpanishFinder()
    finderTwo = EnglishFinder()
    
    print(finderOne.find("Hola"))
    print(finderTwo.find("Hello"))