class Node:
    def __init__(self,key,val):
        self.key=key
        self.val=val
        self.freq=1
        self.prev=None
        self.next=None
class DLL:
    def __init__(self):
        self.head=Node(-1,-1)
        self.tail=Node(-1,-1)
        self.head.next=self.tail
        self.tail.prev=self.head
        self.size=0
    def insertAtHead(self,node):
        front=self.head.next
        self.head.next=node
        node.prev=self.head
        node.next=front
        front.prev=node
        self.size+=1
    def removeNode(self,node):
        before=node.prev
        after=node.next
        before.next=after
        after.prev=before
        self.size-=1
class LFUCache:

    def __init__(self, capacity: int):
        self.mpp={}
        self.fmpp={}
        self.minfreq=1
        self.capacity=capacity
        

    def get(self, key: int) -> int:
        if key  not in self.mpp:
            return -1
        node=self.mpp[key]
        dll=self.fmpp[node.freq]
        dll.removeNode(node)
        if node.freq==self.minfreq and dll.size==0:
            self.minfreq+=1
        node.freq+=1
        if node.freq not in self.fmpp:
            self.fmpp[node.freq]=DLL()
        dll=self.fmpp[node.freq]
        dll.insertAtHead(node)
        return node.val
        

    def put(self, key: int, value: int) -> None:
        if key in self.mpp:
            node=self.mpp[key]
            dll=self.fmpp[node.freq]
            dll.removeNode(node)
            if node.freq==self.minfreq and dll.size==0:
                self.minfreq+=1
            node.freq+=1
            if node.freq not in self.fmpp:
                self.fmpp[node.freq]=DLL()
            dll=self.fmpp[node.freq]
            dll.insertAtHead(node)
            node.val=value
        else:
            if self.capacity<=0:
                return
            if self.capacity==len(self.mpp):
                dll=self.fmpp[self.minfreq]
                node=dll.tail.prev
                dll.removeNode(node)
                del self.mpp[node.key]
            new=Node(key,value)
            self.mpp[key]=new
            if new.freq not in self.fmpp:
                self.fmpp[new.freq]=DLL()
            dll=self.fmpp[new.freq]
            self.minfreq=new.freq
            dll.insertAtHead(new)
        


# Your LFUCache object will be instantiated and called as such:
# obj = LFUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)