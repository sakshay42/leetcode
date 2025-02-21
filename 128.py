class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        dictionary = {}
        out = 0
        for i in nums:
            if i not in dictionary:
                left = dictionary.get(i-1,0)
                right = dictionary.get(i+1,0)
                current = left + right + 1
                dictionary[i] = current
                dictionary[i - left] = current
                dictionary[i + right] = current
                out = max(out,current)
        return out
