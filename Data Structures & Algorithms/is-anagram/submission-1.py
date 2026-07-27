class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s)!=len(t):
            return False
        L={}
        for i in s:
            if i not in L:
                L[i]=1
            else:
                L[i]+=1
        M={}
        for i in t:
            if i not in M:
                M[i]=1
            else:
                M[i]+=1 
        for i in L:
            if i not in M:
                return False

            if L[i]!=M[i]:
                return False
        return True                          
        