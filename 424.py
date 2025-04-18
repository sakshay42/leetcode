class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        left = 0
        window_length =0
        max_length = -float("inf")
        freq = defaultdict(int)
        for right in range(len(s)):
            freq[s[right]] +=1
            window_length = right-left +1
            while right-left+1-max(freq.values()) > k:
                  freq[s[left]] -=1
                  left +=1
            max_length = max(max_length,right-left+1)
        return max_length
