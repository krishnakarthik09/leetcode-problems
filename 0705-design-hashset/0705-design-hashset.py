class MyHashSet:

    def __init__(self):
        self.Data=[[] for _ in range(10**4)]
    def add(self, key: int) -> None:
        index=key%len(self.Data)
        for i in range(len(self.Data[index])):
            if self.Data[index][i]==key:
                return 
        self.Data[index].append(key)

        

    def remove(self, key: int) -> None:
        index=key%len(self.Data)
        for i in range(len(self.Data[index])):
            if self.Data[index][i]==key:
                self.Data[index].remove(key)
                return
        

    def contains(self, key: int) -> bool:
        index=key%len(self.Data)
        for i in range(len(self.Data[index])):
            if self.Data[index][i]==key:
                return True
        return False
        


# Your MyHashSet object will be instantiated and called as such:
# obj = MyHashSet()
# obj.add(key)
# obj.remove(key)
# param_3 = obj.contains(key)