class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        length_s = len(s)
        length_t = len(t)
        top = 0
        if length_s == 0: return True
        for bottom in range(length_t):
            if s[top] == t[bottom]: 
               top +=1
               if top == length_s:return True

            
        return False




## slightyl faster
class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        i = 0
        for c in t:
            if i < len(s) and s[i] == c:
                i += 1
        return i == len(s)
