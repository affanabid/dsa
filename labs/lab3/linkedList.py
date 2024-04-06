class Node:
    def __init__(self , data):
        self.data = data 
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None

    def insert_at_head(self,val):
        new_node = Node(val)
        if self.head is None:
            self.head = new_node
            return
        new_node.next = self.head
        self.head = new_node

    def insert_at_tail(self,val):
        new_node = Node(val)
        if self.head is None:
            self.head = new_node
            return
        temp = self.head
        while temp.next is not None:
            temp = temp.next
        temp.next = new_node

    def insert_before(self , key , val):
        new_node = Node(val)
        if self.head is None:
            self.head = new_node
            return
        temp = self.head
        while temp.next is not None:
            if temp.next.data == key:
                new_node.next = temp.next
                temp.next = new_node
                return
            temp = temp.next

    def insert_after(self , key , val):
        new_node = Node(val)
        if self.head is None:
            self.head = new_node
            return
        temp = self.head
        while temp.next is not None:
            if temp.data == key:
                new_node.next = temp.next
                temp.next = new_node
                return
            temp = temp.next

    def update(self, key ,val):
        temp = self.head
        while temp is not None:
            if temp.data == key:
                temp.data = val
                return
            temp = temp.next
            
    def search(self, val):
        temp = self.head
        while temp is not None:
            if temp.data == val:
                print('Key is present in list')
                return    
            temp = temp.next
        print('key is not present')

    def remove_at_head(self):
        if self.head is None:
            print('List is empty')
        temp = self.head 
        self.head = temp.next
        del temp

    def remove_at_tail(self):
        if self.head is None:
            print('List is empty')
            return
        temp = self.head
        temp2 = self.head
        while temp.next is not None:
            temp2 = temp
            temp = temp.next
        del temp
        temp2.next = None

    def remove_before(self, key):
        if self.head is None:
            print('List is empty')
            return
        temp = self.head
        temp2 = self.head
        while temp.next is not None:
            if temp.next.data == key:
                temp2.next = temp.next
                del temp
                return
            temp2 = temp
            temp = temp.next

    def remove_after(self, key):
        if self.head is None:
            print('List is empty')
            return
        temp = self.head
        temp2 = self.head
        while temp.next is not None:
            if temp.data == key:
                temp.next = temp2.next
                del temp2
                return
            temp = temp.next
            temp2 = temp.next
            
    def display_list(self):
        if self.head is None:
            print('List is empty')
        current_node = self.head 
        while current_node is not None:
            print(current_node.data,end=' ')
            current_node = current_node.next
        print()

    def swap(self):
        if self.head == None:
            return self.head
        elif self.head.next is None:
            return self.head
        else:
            current1 = self.head
            current2 = current1.next
            self.head = current2
            while current2 is not None:
                temp = current2.next
                current2.next = current1
                current1.next = temp
                
                if current1.next is None or current1.next.next is None:
                    
                    break
                current2 = current2.next.next.next
                new_temp = current1.next
                current1.next = current2
                current1 = new_temp
    
    def middle(self):
        current1 = self.head
        current2 = self.head
        while current2 is not None and current2.next is not None:
            current1 = current1.next
            current2 = current2.next.next
        print(current1.data)
    
    def reverse(self):
        if self.head is None:
            return
        prev = None
        current = self.head
        nextNode = None
        while current:
            nextNode = current.next
            current.next = prev
            prev = current
            current = nextNode
        self.head = prev

# def merge(list1, list2):
#     new = LinkedList()
#     current1 = list1.head
#     current2 = list2.head
#     while current1 or current2:
#         if current1:
#             new.insert_at_tail(current1.data)
#             current1 = current1.next
#         if current2:
#             new.insert_at_tail(current2.data)
#             current2 = current2.next
#     return new
    def merge(self, list1, list2):
        while list2:
            nextNode = list1.next
            list1.next = list2
            list1 = list2
            list2 = nextNode
        
            
def main():
    obj= LinkedList()
    obj.insert_at_head(1)
    obj.insert_at_tail(3)
    obj.insert_at_tail(5)

    ob = LinkedList()
    ob.insert_at_head(2)
    ob.insert_at_tail(4)
    ob.insert_at_tail(6)
    ob.insert_at_tail(8) 
    obj.middle()
    ob.middle()
    # obj.insert_at_tail(5)

    # obj.insert_at_tail(9)
    # obj.insert_at_tail(6)
    # obj.insert_at_tail(6)
    # obj.insert_at_tail(4)
    # obj.insert_before(7,3)
    # obj.insert_after(7,8)
    # obj.update(6,4)
    # obj.search(7)
    # obj.remove_at_head()
    # obj.remove_at_tail()
    # obj.display_list()
    # obj.remove_before(8)
    # obj.display_list()
    # obj.remove_after(9)
    obj.display_list()
    obj.merge(obj.head, ob.head)
    # obj.display_list()
    # obj.reverse()
    # obj.swap()
    obj.display_list()
        
main()