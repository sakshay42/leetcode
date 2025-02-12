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
