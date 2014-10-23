'''The abstract factory pattern provides a way to encapsulate a group of
individual concreate factories that have a common theme without specifying 
their concrete classes.

Because abstract factory only returns a reference (pinter) to the abstract 
product, The client does not need to / care the concreate type of the product.
'''

ROBUST = 0
class Shape(): #This class is the main factory class
    total=0
    def __init__(self):
        self.total=self.total+1

    def draw(self): #Abstract Function
        raise NotImplementedError('Should Have implemented This')
        
class Circle(Shape): #Inherits Shape class
    def draw(self): #Implements the abstract function
        print "Circle" + "Drawnn"
        
class Square(Shape): #Inherits shape class
    def draw(self): #Implments the abstract function
        print "Square" + " Drawnn"

class Ellipse(Shape):#Inherits shape class
    def draw(self): #Implements the abstract function
        print "Ellipse" + " Drawnn"

class Rectangle(Shape):#Inherits shape class
    def draw(self):#Implements the abstract function
        print "Rectangle" + " Drawnn"
        
class Factory(): #Abstract Class 
    # @staticmethod
    def createCurvedInstance(): #Abstract function
        raise NotImplementedError('Should Have implemented This')
    def createStraightInstance():#Abstract Function
        raise NotImplementedError('Should Have implemented This')

class SimpleShapeFactory(Factory):#Inherits Factory 
    def createCurvedInstance(self):#Creates Circle object
        c1=Circle()
        return c1
    def createStraightInstance(self):#Creates Square object
        s1=Square()
        return s1
        
class RobustShapeFactory(Factory):#Inherits Factory 
    def createCurvedInstance(self):#Creates Ellipse object 
        c1=Ellipse()
        return c1
    def createStraightInstance(self):#Creates Ellipse object
        s1=Rectangle()
        return s1

def main():
    if ROBUST==1:	#Checks the global variable ROBUST
        s1=SimpleShapeFactory()
    else:    
        s1=RobustShapeFactory()        
    s4=[Shape,Shape,Shape]   #Creates List of shape objects
    s4[0]=s1.createCurvedInstance()
    s4[1]=s1.createStraightInstance() 
    s4[2]=s1.createCurvedInstance()
    for n in s4:
        n.draw() #Calls Draw objects

if __name__=='__main__':
    main()
