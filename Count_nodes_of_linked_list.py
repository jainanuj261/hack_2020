clas Node:
    def __init__(self,data):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None

    def append(self,new_node):
        if self.head is None:
            self.head = new_node
            return
        n = self.head
        while n.next is not None:
            n = n.next
        n.next = new_node

    def printNodes(self):
        print("Your Nodes in the Linked List Are:")
        n = self.head
        while n is not None:
            print(n.data, end=" ")
            n = n.next
        print()

    def getCount(self,head_node):
        count = 0
        if head_node is None:
            return count
            print("Count:",count)
        while head_node is not None:
            count = count+1
            head_node = head_node.next
        print("Count:",count)
    
    def getNth(self,head, k):
        count = 0
        while head is not None:
            count = count+1
            if count == k:
                return head.data
            head = head.next

    def findMid(self,head):
        length = 0
        head_node = head
        if head is None:
            return
        while head_node is not None:
            length+=1
            head_node = head_node.next
        middle = length//2
        for i in range(middle):
            head = head.next
        return head.data

if __name__ == '__main__':
    t = int(input("Enter the number of nodes:"))
    a = LinkedList()
    nodes = list(map(int,input().split()[:t]))
    for x in nodes:
        node = Node(x)
        a.append(node)
    
    a.printNodes()
    a.getCount(a.head)
    # m = a.getNth(a.head,5)
    # print(" Value at index 5 is:",m) # for users understanding index starts from 1
    
    mid = a.findMid(a.head)
    print("Mid Value:",mid)
