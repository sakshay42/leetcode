class Solution:
    def summaryRanges(self, nums: List[int]) -> List[str]:
        if len(nums)==0: return []
        dictionary = {nums[0]:0}
        for i in nums[1:]:
            updated = False
            for j in dictionary:
                if j + dictionary[j] +1 == i:
                    dictionary[j] += 1 
                    updated = True
                    break
            if not updated:
                dictionary[i] = 0
        out = []
        for j in dictionary:
            out.append(str(j) + "->"+str(j+dictionary[j]) if dictionary[j]!= 0 else str(j))
        return out
                
            
        
