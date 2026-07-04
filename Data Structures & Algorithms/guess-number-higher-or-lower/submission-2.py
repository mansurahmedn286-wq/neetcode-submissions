# The guess API is already defined for you.
# @param num, your guess
# @return -1 if num is higher than the picked number
#          1 if num is lower than the picked number
#          otherwise return 0
# def guess(num: int) -> int:

class Solution:
    def guessNumber(self, n: int) -> int:
        t,b=1,n
        while t<=b:
            m=(t+b)//2
            r=guess(m)
            if r==0:
                return m
            elif r==-1:
                b=m-1
            else:
                t=m+1
        return "not in the range"                
        