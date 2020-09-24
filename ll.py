class Node:
    def __init__(self,data):
        self.data = data
        self.link=None
class LL:
    def __init__(self):
        self.start=None
    def append(self,data):
        p=self.start
        temp=Node(data)
        if self.start is None:
            self.start=temp
        else:
            while p.link is not None:
                p=p.link
            p.link=temp
    def addbefore(self,befdata,data):
        p=self.start
        temp=Node(data)
        if self.start.data==befdata:
            temp.link=self.start
            self.start=temp
            return
        while p is not None:
            if p.link.data == befdata:
                temp.link=p.link
                p.link=temp
                break
            p=p.link
    def addafter(self,aftdata,data):
        p=self.start
        temp=Node(data)
        while p is not None:
            if p.data == aftdata:
                temp.link=p.link
                p.link=temp
                break
            p=p.link
    def __str__(self):
        p=self.start
        if self.start is None:
            return 'Empty List'
        llstr=''
        while p is not None:
            llstr+=str(p.data)+'-->'
            p=p.link
        llstr+='End'
        return llstr
    def create_llist(self):
        p=self.start
        n=int(input("How many elements do you want to add: "))
        if n>0:
            for x in range(n):
                d=int(input("Enter data: "))
                temp=Node(d)
                if p is None:
                    self.start=temp
                else:
                    p.link=temp
                    p=p.link
if __name__ == '__main__':
    llist=LL()
    for x in range(0,11):
        llist.append(x)
    llist.addbefore(1,0)
    llist.addafter(10,11)
    
    print(llist)