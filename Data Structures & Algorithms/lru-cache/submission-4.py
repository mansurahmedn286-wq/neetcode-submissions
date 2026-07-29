from collections import deque
class LRUCache:

    def __init__(self, capacity: int):
        self.L=deque()
        self.capacity=capacity

        

    def get(self, key: int) -> int:
        for i in self.L:
            if i[0]==key:
                self.L.remove(i)
                self.L.append(i)
                return i[1]
        return -1


        

    def put(self, key: int, value: int) -> None:
        for i in self.L:
            if i[0]==key:

                self.L.remove(i)
                self.L.append([key,value])
                return
        if len(self.L)<self.capacity:
            self.L.append([key,value])
            return
        self.L.popleft()
        self.L.append([key,value])   



        
