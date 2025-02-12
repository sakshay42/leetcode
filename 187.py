class Solution:
    def findRepeatedDnaSequences(self, s: str) -> List[str]:
        current_string = s[:10] #start with first string of length 10
        counter = {current_string:1} 
        
        for i in range(1,len(s)-9):
            current_string = current_string[1:] + s[i+9] #remove the first and add next letter
            counter[current_string] = counter.get(current_string,0)+1 #check if it is already there
        return([dna for dna,freq in counter.items() if freq >=2])
        
