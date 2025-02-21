class Solution:
    def romanToInt(self, s: str) -> int:
        values = {"I":1, "V": 5, "X":10, "L": 50, "C":100, "D":500, "M":1000}
        out = 0
        right = 0
        while right < len(s):
            if right == len(s)-1: out += values[s[right]]
            else:
                if values[s[right]] < values[s[right+1]]:
                    out += values[s[right+1]] -values[s[right]]
                    right +=1
                else: out+= values[s[right]]
            right +=1
        return out
