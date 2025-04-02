class Solution:
    def longestPalindrome(self, s: str) -> str:
        max_palindrome = ""
        for i in range(len(s)):
            left,right = i,i
            curr = s[i]

            #look for odd length palindromes
            while left > -1 and right < len(s) and s[left] == s[right]:
                left -= 1
                right +=1
            curr = s[left + 1:right]
            max_palindrome = curr if len(curr) > len(max_palindrome) else max_palindrome
            
            #look for even length palindromes
            left,right = i,i+1
            while left > -1 and right < len(s) and s[left] == s[right]:
                left -= 1
                right +=1
            curr = s[left + 1:right]
            max_palindrome = curr if len(curr) > len(max_palindrome) else max_palindrome

        return max_palindrome
                
