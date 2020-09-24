class Node:
    def __init__(self,data):
        self.prev=None
        self.data=data
        self.next=None
class DoublyLL:
    def __init__(self):
        self.start=None
    def append(self,data):
        p=self.start
        temp=Node(data)
        if p is None:
            self.start=temp
            return
        while p.next is not None:
            p=p.next
        p.next=temp
        temp.prev=p
    def addafter(self,data,aftdata):
        p=self.start
        temp=Node(data)
        i=0
        while p.next is not None:
            p=p.next
            if p.data==aftdata:
                i=1
                break
        if i:
            prev=p.next
            p.next=temp
            temp.prev=p
            temp.next=prev
        else:
            print("Data not found")
    def addbefore(self,data,befdata):
        p=self.start
        temp=Node(data)
        while p.next is not None:
            if p.next.data==befdata:
                temp.next=p.prev
                temp.prev=p
                p.next.prev=temp
                p.prev.next=temp
            p=p.next
    def reversal(self):
        p1=self.start
        p2=p1.next
        p1.next=None
        p1.prev=p2
        while p2 is not None:
            p2.prev=p2.next
            p2.next=p1
            p1=p2
            p2=p2.prev
        self.start=p1

if __name__=='__main__':
    llist=DoublyLL()
    llist.append(1)
    llist.append(2)
    #llist.addbefore(3,2)
    llist.reversal()