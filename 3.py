class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        window = ""
        out = 0
        left =0
        for right in range(0,len(s)):
            x= s[right]
            while x in window and right > left:
                left += 1
                window = window[1:]
            window += s[right]
            out = max(out,right- left +1)
        return(out)


#same using sets

class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        window = set()
        left =0
        out = 0
        for right in range(len(s)):
            while s[right] in window:
                    window.remove(s[left])
                    left +=1
            window.add(s[right])
            out = max(right-left+1,out)
        return out
