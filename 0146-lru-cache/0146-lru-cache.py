class Node:
    def __init__(self,key,val):
        self.key=key
        self.val=val
        self.next=None
        self.prev=None
        self.nodekey=key



class LRUCache:

    def __init__(self, capacity: int):
        self.capacity=capacity
        self.head=Node(-1,-1)
        self.tail=Node(-1,-1)
        self.head.next=self.tail
        self.tail.prev=self.head
        self.mpp={}
        

    def get(self, key: int) -> int:
        if key not in self.mpp:
            return -1
        node=self.mpp[key]
        self.deletenode(node)
        self.insertAtHead(node)
        return node.val




    def deletenode(self,node):
        prev=node.prev
        front=node.next
        prev.next=front
        front.prev=prev
    def insertAtHead(self,node):
        front=self.head.next
        self.head.next=node
        node.prev=self.head
        node.next=front
        front.prev=node
        

    def put(self, key: int, value: int) -> None:
        if key in self.mpp:
            node=self.mpp[key]
            node.val=value
            self.deletenode(node)
            self.insertAtHead(node)
        else:
            if len(self.mpp)==self.capacity:
                node=self.tail.prev
                del self.mpp[node.nodekey]
                self.deletenode(node)
            newnode=Node(key,value)
            self.mpp[key]=newnode
            self.insertAtHead(newnode)

        


# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)