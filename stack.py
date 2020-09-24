class EmptyStackError(Exception):
    pass
class Stack:
    def __init__(self):
        self.items=[]
    def isEmpty(self):
        return bool(not self.items)
    def count(self):
        return len(self.items)
    def push(self,item):
        return self.items.append(item)
    def pop(self):
        if not self.isEmpty():
            return self.items.pop()
        raise EmptyStackError("Stack is Empty")
    def peek(self):
        return self.items[-1]
    def print(self):
        if self.isEmpty(): return print("Stack is Empty")
        return print(self.items)
if __name__=='__main__':
    x=Stack()
    while True:
        print('''1. Push an Element
2. Pop an Element
3. Count The Stack
4. Is the Stack Empty
5. Peek The Stack
6. Display the Stack''')
        i=int(input("Enter Your Choice : "))
        if i==0:
            break
        elif i==1:
            item=input("Enter item")
            x.push(item)
        elif i==2:
            print("Popped Element:",x.pop())
        elif i==3:
            print("Total Elements:",x.count())
        elif i==4:
            print(x.isEmpty())
        elif i==5:
            print(x.peek())
        elif i==6:
            x.print()
        elif i not in range(7): print("Wrong Choice, Try again!!")
