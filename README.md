
#Patrones de diseño

    
##Patrones de arquitectura
    Son los patrones que indican como se estructuran los proyectos
     ej: Layers, ModelViewController(MVC),EventDrivenArchitecture(EDA)
    
    
##Patrones de diseño
    Son los patrones que indican como se implementan las clases o modulos
    ej: Factory Method, Facade, Strategy, Observer, Adapter, Singleton.
      
###Patrones creacionales:
    Son patrones que solucionan problemas de creación de objetos. Permiten encapsular y abstraer dicha creación.
  - [Factory Method] (https://github.com/alejo-moreno/designpatterns/blob/master/Design_Pattern/Creational/FactoryMethod.py) `Patron  de diseño de creación de clase`: Crea una instancia de varias clases derivadas
  - [Abstract Factory] (https://github.com/alejo-moreno/designpatterns/blob/master/Design_Pattern/Creational/AbstractFactory.py) `Patron de diseño de creación de objeto`: Crea una instancia de varias familias de clases
  - [Builder] (https://github.com/alejo-moreno/designpatterns/blob/master/Design_Pattern/Creational/Builder.js) `Patron de diseño de creación de objeto`: Separa la construccion de un objeto de su representacion
  - [Singleton] (https://github.com/alejo-moreno/designpatterns/blob/master/Design_Pattern/Creational/Singleton.js)`Patron de diseño de creación de objeto` : Una clase de la cual solo una instancia puede existir  
  - [Prototype] `Patron de diseño de creación de objeto` : Una instancia que puede ser clonada completamente para su uso
  
  
####Principio Solid
- [x] Single responsibility: La clase solo debe responder para lo que fue creada
- [x] Open Closed: Abierta para delegar caracteristicas pero cerrada en cuanto al comportamiento de la solución.
- [x] Liskov Substitution: Poder sustituir una clase heredada por la clase base (Perro -> Animal)
- [x] Interface Segregation: Poder Hacer interfaces detalladas para requerimientos especificos de cliente (Facade)
- [x] Dependency Inversion: La dependencia debe ser de las clases base más no de las heredadas
      
###Patrones estructurales:
    Son patrones que solucionan problemas de composición (agregación) de clases y objetos        
  - **Adapter**: Adapta una interfaz para que pueda ser utilizada por una clase que de otro modo no podría utilizarla.
  - **Facade**: Provee de una interfaz unificada simple para acceder a una interfaz o grupo de interfaces de un subsistema.
  - **Decorator**: Añade comportamientos o responsabilidades a los objetos dinamicamente.
          
###Patrones de comportamiento:
    Son patrones que guian la interacción entre los objetos            
  - **Chain of responsibility**: Encadena una petición a varios objetos para que cada uno interactue especificamente.
  - **Command**: Encapsula una petición de comandos en un solo objeto.
  - **Interpreter**: Una manera de incluir elementos del lenguaje en un programa.
  - **Iterator**: Acceso secuencial a los elementos de una colección.
  - **Mediator**: Define una comunicación simplificada entre clases (APIs).
  - **Memento**:  Captura y restaura el estado interno de un objeto.
  - **Observer**: Una forma de notificar cambios a varias clases (Publish & Subscribe)
  - **State**: Altera el comportamiento de un objeto cuando cambia de estado (Wizards)
  - **Strategy**: Encapsula un algoritmo dentro de una clase
  - **Template Method**: Difiere los pasos exactos de un algoritmo a una subclase
  - **Visitor**: Define una nueva operación a una clase sin cambiarla 

      
##Idioms/Modismos
    Son las ventajas o carácterisiticas del lenguaje especifico aplicado
      ej: Convenciones del lenguaje (Interfaces, Abstract, Herencia), Uso de memoria.
        
        
##Bibliografia:

- [Source Making Design Patterns] (https://sourcemaking.com/design_patterns)
- [Structure and Interpretation of Computer Programs] (https://mitpress.mit.edu/sicp/full-text/book/book.html)
- [Abstract Factory Javascript] (http://www.dofactory.com/javascript/abstract-factory-design-pattern)
- [NodeJS Design Patterns] (https://blog.risingstack.com/fundamental-node-js-design-patterns)
