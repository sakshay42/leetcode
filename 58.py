class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        n = len(s)
        left= n-1
        right = n-1
        out = 0 
        while left <= right and left >=0 and right >=0:
            while s[right]==" ":
                left -=1
                right -=1
            if s[left] ==" ":
                right = left-1
            else: 
                out =max(out,right-left +1)
                left = left -1
                
        return out
