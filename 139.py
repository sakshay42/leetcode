class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        dp = [False]*(len(s)+1)
        dp[len(s)]=True
        for right in range(len(s)-1,-1,-1):
            print(dp)
            for word in wordDict:
                if right+len(word)<= len(s):
                    if s[right:right+len(word)] == word:
                        dp[right] = dp[right+len(word)]
                    
                    if dp[right]:  # Early exit: no need to check further
                        break
        return dp[0]
