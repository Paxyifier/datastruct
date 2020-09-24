class Node:
    def __init__(self,data):
        self.link=None
        self.data=data
class Stack:
    def __init__(self):
        self.end=None
    def push(self,data):
        temp=Node(data)
        temp.link=self.end
        self.end=temp
    def pop(self):
        if self.end is None: return print("Empty Stack")
        temp=self.end.data
        self.end=self.end.link
        return print(temp)
    def display(self):
        p=self.end
        if p is None: return print("Empty Stack")
        print("Top",end="")
        while p:
            try:
                print("--",end="")
                print(p.data,end="")
            except:
                pass
            p=p.link
    def isEmpty(self):
        if self.end==None: return True
        else: return False
    def peek(self):
        if self.end is None: return print("Empty Stack")
        return print(self.end.data)
stck=Stack()
while True:
    print("\n1. Push\n2. Pop\n3. Display\n4. Is Empty\n5. Peek")
    i=int(input("Enter Choice : "))
    if i==0:break
    elif i==1:
        x=input("Enter data: ")
        stck.push(x)
    elif i==2:
        stck.pop()
    elif i==3:
        stck.display()
    elif i==4: print(stck.isEmpty())
    elif i==5: stck.peek()
