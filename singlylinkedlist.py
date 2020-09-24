class Node:
    def __init__(self,data=None):
        self.data=data #Assign data
        self.link=None #Initialize as null
class LinkedList:
    def __init__(self):
        #initialize start
        self.start=None
     #Works
    def print(self):print(self)
    # Works by using __str__ default of python.
    #Works
    def __str__(self):
        p=self.start
        if p is None:
            return 'LL is empty'
        # Returning if the start points to None.
        # If not then a string is created.
        # It stores the value of all data inside the linked list.
        llstr = ""
        while p:
            # Here first data is typecasted into string as the data can be of different types.
            llstr += str(p.data)
            # This is an if loop to check if the node currently being pointed is the last or not.
            if p.link is None:
                # If it is the last, then it simply returns the string.
                # This is the only return statement because the last iteration of the while loop is always exited at this line.
                return llstr
            # This is a seperator between two elements. It is placed after the return statement so as to exclude a extra seperator in the output
            llstr+='-->'
            p = p.link
    #Works
    def append(self,nextval):
        # This method simply adds values to the linked list.
        p=self.start
        # temp variable here is the temporary carrier of node object.
        temp=Node(nextval)
        # The following if statement checks if the linked list is empty.
        if p is None:
            # If the linked list is empty then first node has to be directly referenced to the self.start instance variable of linked list
            self.start=temp
            # The loop is exited as the next loop need not occur as this would be the first node.
            return
        # When the 
        while p.link is not None:
            p=p.link
        p.link=temp
    #Works
    def addstart(self,data):
        temp=Node(data)
        temp.link=self.start
        self.start=temp
    #Works
    def count(self):
        p=self.start
        n=0
        while p:
            n+=1
            p=p.link
        print(n)
    #Works
    def reversal(self):
        prev=None
        p=self.start
        while p is not None:
            next=p.link
            p.link=prev
            prev=p
            p=next
        self.start=prev
    #Works
    def search(self,val):
        p=self.start
        n=0
        llstr=str(val)+' found at '
        l=0
        while p:
            n+=1
            if val==p.data:
                if l:llstr+=' and '
                llstr +=str(n)
                l+=1
            p=p.link
        if l:print(llstr)
    #Works
    def posinsert(self,data,pos):
        p=self.start
        temp=Node(data)
        if pos==1:
            temp.link=self.start
            self.start=temp
            return
        i=0
        while p is not None and i<pos-1:
            i+=1
            p=p.link
        if p is None:
            print('You can insert only upto position ',i)
        else:
            temp.link=p.link
            p.link=temp
    #Works
    def pop(self):
        p=self.start
        if not self.start:return print('Empty Linked List')
        if not p.link:
            self.start=None
            return print(p.data)
        while p.link is not None:
            if p.link.link is None:
                temp=p.link.data
                p.link=None
                return print(temp)
            else:
                p=p.link
    #Works
    def __getitem__(self,pos):
        p=self.start
        n=0
        while p:
            if n==pos:return p.data
            p=p.link
            n+=1
        
    def create_llist(self):
        p=self.start
        n=int(input("How many elements do you want to add: "))
        if n>0:
            for x in range(n):
                d=int(input("Enter data: "))
                temp=Node(d)
                if p is None:
                    self.start=temp
                    p=self.start
                else:
                    p.link=temp
                    p=p.link
    def deleteatstart(self):
        p=self.start
        self.start=p.link
    def deleteelm(self,data):
        if self.start==None:
            print('No element to delete!!')
            return
        if self.start.data==data:
            self.start=self.start.link
            return
        p=self.start
        while p.link:
            if p.link.data==data:
                break
            p=p.link
        if not p.link:
            print("Element not found!!")
        else:
            p.link=p.link.link
            print("Element successfully deleted!!")
if __name__=='__main__':
    llist=LinkedList()
    llist.create_llist()
    while True:
        print("1. Print")
        print("2. Count")
        print("3. Search an element")
        print("4. Insert at end")
        print("5. Delete at end")
        print("6. Delete by value")
        print("7. Delete First Element")
        print("8. Insert at position")
        print("9. Reversing the LList")
        opt = int(input("Enter Choice : "))
        if opt == 1:
            llist.print()
        elif opt == 2:
            llist.count()
        elif opt == 3:
            ip=int(input("Enter data for Search"))
            llist.search(ip)
        elif opt == 4:
            ip=int(input("Enter data for input : "))
            llist.append(ip)
        elif opt == 5:
            llist.pop()
        elif opt == 6:
            ip=int(input("Enter the element to be deleted : "))
            llist.deleteelm(ip)
        elif opt == 7:
            llist.deleteatstart()
        elif opt == 8:
            ip1=int(input("Enter the position at which you want to delete : "))
            ip2=int(input("Enter the data you want to insert : "))
            llist.posinsert(ip2,ip1)
        elif opt == 9:
            llist.reversal()