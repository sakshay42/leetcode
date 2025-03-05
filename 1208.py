class Solution:
    def equalSubstring(self, s: str, t: str, maxCost: int) -> int:
        out = -float("inf")
        cost = 0
        left = 0
        for right in range(len(s)):
            cost += abs(ord(s[right]) - ord(t[right]))

            while cost > maxCost:
                cost -= abs(ord(s[left]) - ord(t[left]))
                left +=1
            out = max(out,right-left+1)
        return out
