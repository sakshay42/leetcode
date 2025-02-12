class Solution:
    def findLHS(self, nums: List[int]) -> int:
        track = {}
        for i in nums:
            track[i] = track.get(i, 0) + 1        #get(i,0) = value of i if i is present or 0 otherwise

        out= 0 
        for num in track: 
            # to check for length of a subsequence just need to how frequently n and n+1 appear.
            if num + 1 in track:
                out = max(out, track[num] + track[num + 1])
        
        return out
            
                
           
