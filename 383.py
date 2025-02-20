class Solution(object):
    def canConstruct(self, ransomNote, magazine):
        """
        :type ransomNote: str
        :type magazine: str
        :rtype: bool
        """
        counter = {}
        for i in magazine:
            counter[i] = counter.get(i,0)+1
        for j in ransomNote:
            if j in counter and counter[j] >0:
                counter[j] -=1
            else: return False
        return True
