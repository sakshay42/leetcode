class Solution:
    def maxVowels(self, s: str, k: int) -> int:
        vowels = set(['a', 'e', 'i', 'o', 'u'])
        
        current = 0
        out = 0
        left = 0
        n = len(s)
        
        for right in range(n):
            if s[right] in vowels:
                current += 1
                
            # When the window reaches size k, adjust the left pointer
            if right - left + 1 > k:
                if s[left] in vowels:
                    current -= 1
                left += 1
            
            # Update the result
            if right - left + 1 == k:
                out = max(out, current)
        
        return out


### optimal

class Solution:
    def maxVowels(self, s: str, k: int) -> int:
        vowels = set(['a', 'e', 'i', 'o', 'u'])
        
        count = sum(1 for i in range(k) if s[i] in vowels)
        out =count
        for i in range(len(s)-k):
            if s[i+k] in vowels:
                count +=1
            if s[i] in vowels:
                count -=1
            out = max(out,count)
        return out
