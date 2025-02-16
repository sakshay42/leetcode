class Solution:
    def maxOperations(self, nums: List[int], k: int) -> int:
        freq = {}
        for i in nums:
            freq[i] = freq.get(i,0)+1

        print(freq)
        out = 0
        for num in freq:
            if num == k/2:
                out += freq[num]//2
            elif num < k/2: out += min(freq[num],freq.get(k-num,0))
            
        return(out)
