class LRUCache:

    def __init__(self, capacity: int):
        self.capacity=capacity
        self.L={}

        

    def get(self, key: int) -> int:
        if key in self.L:
            val = self.L.pop(key)
            self.L[key] = val
            return val
        return -1






       


        

    def put(self, key: int, value: int) -> None:
        if key in self.L:
            self.L.pop(key)
            self.L[key]=value
            return 
        if len(self.L)<self.capacity:
                
            self.L[key]=value
            return
        for i in self.L:
            self.L.pop(i)
            break
        self.L[key]=value                 
            

        
