#Clases de subsistema 
class Scanner:
    def __init__(self):
        self.name = "Scanner"
        
class Parser:
    def __init__(self):
        self.name = "Parser"

#Facade       
class Compiler:
    def __init__(self):
        self.name = "Compiler"
        self.scanner = Scanner()
        self.parser = Parser()
        
    def compile(self):
        print("Compiling...")
        print("Scanning {}".format(self.scanner.name))
        print("Parsing {}".format(self.parser.name))    
        
if __name__ == "__main__":
    compiler = Compiler()
    compiler.compile();