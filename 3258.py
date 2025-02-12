class Solution:
    def countKConstraintSubstrings(self, s: str, k: int) -> int:
        out = 0
        window_counts = [0,0]#number of zeros and ones in the window
        left = 0
        for right in range(0,len(s)):
            window_counts[int(s[right])] +=1 
            while min(window_counts) > k:
                window_counts[int(s[left])] -= 1
                left += 1
            out += (right - left + 1)
        return(out)
            
