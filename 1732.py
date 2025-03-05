class Solution:
    def largestAltitude(self, gain: List[int]) -> int:
        curr = 0
        out = 0
        for i in range(0,len(gain)):
            curr +=gain[i]
            out = max(out,curr)

        return out
