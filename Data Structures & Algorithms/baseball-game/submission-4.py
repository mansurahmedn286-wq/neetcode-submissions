class Solution:
    def calPoints(self, operations: List[str]) -> int:
        L=[]
        a=['+','C','D']
        for i in range(len(operations)):
            if operations[i] not in a:

                L.append(int(operations[i]))
            else:
                if operations[i]=='+':
                    L.append(L[len(L)-1]+L[len(L)-2])
                    
                elif operations[i]=='C':
                    L.pop()
                elif operations[i]=='D':
                    L.append(2*int(L[len(L)-1]))
        return sum(L)           
    





        