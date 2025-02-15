"""
class Solution:
    def findRepeatedDnaSequences(self, s: str) -> List[str]:
        current_string = s[:10]
        counter = {current_string:1}
        
        for i in range(1,len(s)-9):
            current_string = current_string[1:] + s[i+9]
            counter[current_string] = counter.get(current_string,0)+1
        return([dna for dna,freq in counter.items() if freq >=2])
"""

class Solution:
    def findRepeatedDnaSequences(self, s: str) -> List[str]:
        n = len(s)
        out = set()
        counter = {s[:10]:1}
        for i in range(1,n-9):
            window = s[i:i+10]
            if  window in counter:
                out.add(window)
            else: counter[window] = 1
        return( list(out) )
