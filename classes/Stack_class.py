class Stack:  
    def __init__(self,size = 16):  
        self.stack = []  
        self.size = size  

    def SetSize(self, size):  
        self.size = size  

    def isEmpty(self):  
        if len(self.stack) == 0:
            return True
        return False

    def isFull(self):  
        if len(self.stack) == self.size:  
            return True  
        return False  

    def push(self, obj):  
        if self.isFull():  
            raise Exception("StackOverFlow")  
        else:  
            self.stack.append(obj)  

    def pop(self):  
        if self.isEmpty():  
            raise Exception("StackIsEmpty")  
        else:  
            return self.stack.pop()  

    def show(self):  
        print(self.stack)  


# test
if __name__ == '__main__':
    s = Stack(3)
    s.push(5)
    s.push(6)
    print s.isFull()
    s.push(8)
    print s.isFull()

    s.show()

    s.pop()
    s.pop()
    print s.isEmpty()
    s.pop()
    print s.isEmpty()
    s.show()


