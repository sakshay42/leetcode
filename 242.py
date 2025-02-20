class Solution(object):
    def isAnagram(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        counter = {}
        if len(s)!= len(t): return False
        for i in s:
            counter[i] = counter.get(i,0)+1
        for j in t:
            if j in counter and counter[j]>0:
                counter[j] -=1
            else: return False
        return True
