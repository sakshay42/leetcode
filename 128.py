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


######## quick

class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        # edge cases
        # nums is empty, return 0
        if not nums:
            return 0

        # duplicate not included
        unique_num = set(nums)

        max_len = 1
        curr_len = 0

        for num in unique_num:
            if (num - 1) not in unique_num: # num -1 not in the list, then num is the start of the subsequence
                curr_num = num
                curr_len = 1 # new sequence
                # expand this subsequence, check curr_num + 1
                while (curr_num + 1) in unique_num:
                    curr_len += 1
                    curr_num += 1 # move to next num

                max_len = max(max_len, curr_len)

        return max_len 
