class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        L=[]

        M=[]
        N=[]
        for i in range(len(strs)):
            j=sorted(strs[i])
            if j not in L:
                L.append(j)
                for k in range(len(strs)):
                    if sorted(strs[k])==j:
                        M.append(strs[k])
                N.append(M)
                M=[]
        return N                





               
                    





                
            
               
                


         

            
        