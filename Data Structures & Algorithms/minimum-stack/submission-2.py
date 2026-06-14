class MinStack:

    def __init__(self):
        self.stack=[]
        self.minstack=[]

        

    def push(self, val: int) -> None:
        self.stack.append(val)
        if self.minstack!=[]:
            self.minstack.append(val)
        else:
            if self.minstack!=[]:
                if  self.minstack[0]>val:
                       self.minstack[0]=val



            


        

        

    def pop(self) -> None:
        if not self.stack==[]:
           self.stack.pop()
        

    def top(self) -> int:
        if not self.stack==[]:
            return self.stack[len(self.stack)-1]

        

    def getMin(self) -> int:
        if not self.stack==[]:
            return min(self.stack)

        
