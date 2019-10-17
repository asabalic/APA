import numpy as np
import sys
import time
start_time = time.time()


class Node:
    def __init__(self, iden, loci, value):
        self.iden = iden
        self.loci = loci
        self.value = value
        self.next = None

    def setNext(self, newnext):
        self.next = newnext

class LinkedList:
    def __init__(self):
        self.head = None
        self.tail = None

    def add(self, item, loci, value):
        """Adding nodes to linked list"""
        temp = Node(item, loci, value)
        temp.setNext(self.head)
        self.head = temp


    def insertionSort(self,h):
        """Insertion sort on linked list"""
        if h == None:
            return None
        #Make the first node the start of the sorted list.
        sortedList= h
        h=h.next
        sortedList.next= None
        while h != None:
            curr= h
            h=h.next
            if comparison(curr.loci, sortedList.loci) == False:
                curr.next= sortedList
                sortedList= curr
            else:
                search= sortedList
                while search.next!= None and comparison(curr.loci, search.next.loci) == True:
                    search= search.next
                curr.next= search.next
                search.next= curr
        return sortedList
        
    
    def distance(self, head, k):
        """Checking distance condition for a given k"""
        f= open("output.txt","w")
        counter = 0
        while head.next!= None:
            if get_info(head.next.loci) != get_info(head.loci):
                t = (head.loci, counter)
                f.write(str(get_info(head.loci)) + '\t' + str(counter) + '\n') 
                counter = 0
            else:  
                nex = head.next
                while nex != None and get_info(nex.loci) == get_info(head.loci):
                    a = np.asarray(head.value)
                    b = np.asarray(nex.value)
                  
                    if (np.linalg.norm(a-b)) <= k:
                        counter +=1
                    nex = nex.next
            head = head.next
        t = (head.loci, counter)  
        f.write(str(get_info(head.loci)) + '\t' + str(counter) + '\n') 
        f.close()
        return l
            
    def add_list_item(self, item):
        """add an item at the end of the list"""

        if not isinstance(item, Node):
            item = LinkedList(item)
        if self.head is None:
            self.head = item
        else:
            self.tail.next = item
        self.tail = item
        return item
       

    def printList(self,d):
        """Printing Linked List"""
        while d:
            s = d.loci
            d = d.next
            print (s)

def get_number(string):
    """Extracting number of chromosome arm"""
    if 'q' in string:
        num = float(string.partition('q')[0])
    else:
        num = float(string.partition('p')[0])
        
    return num

def get_letter(string):
    """Extracting letter of chromosome arm"""
    if 'q' in string:
        letter = string.partition('q')[1]
    else:
        letter = string.partition('p')[1]
  
    return letter

def get_info(string):
    """Extracting entire identifier of chromosome arm"""
    number = get_number(string)
    letter = get_letter(string)
    loci_info = str(int(number))+letter
    
    return loci_info

def comparison(a,b):
    """Comparison of chromosome arm names"""
    if get_number(a) > get_number(b):
        return True
    if get_number(a) < get_number(b):
        return False
    if get_number(a) == get_number(b):
        if get_letter(a) < get_letter(b):
            return False
        else:
            return True  

    
def iterator(filename):
    """Iterating through file"""

    fd = open(filename,"r")
    for line in fd:
        fields = line.strip().split()
        iden = fields[0]
        loci = fields[1]
        s = fields[2]
        new = s[s.find("(")+1:s.find(")")]
        value = new.rpartition(',')
        value1 = float(value[0])
        value2 = float(value[2])
        value = (value1,value2)
        item = Node(iden,loci,value)
        llist.add_list_item(item)

    fd.close()
 

    
if __name__=='__main__': 
    
    llist = LinkedList() 
    iterator(filename = sys.argv[1])
    l=llist.insertionSort(llist.head)
    llist.distance(l,float(sys.argv[2]))
    end_time = time.time()
    print("Total execution time: {}".format(end_time - start_time))   

    
