class Solution(object):
    def checkInclusion(self, s1, s2):
        """
        :type s1: str
        :type s2: str
        :rtype: bool
        """
        m = len(s1)
        n = len(s2)
        if n< m: return False
        counter = {}
        for i in s1:
            counter[i] = counter.get(i,0)+1
        window_counter = {}
        for i in range(m):
            window_counter[s2[i]] = window_counter.get(s2[i],0)+1
        if window_counter == counter: return True
        for i in range(n-m):
            window_counter[s2[i+m]] = window_counter.get(s2[i+m],0) + 1
            window_counter[s2[i]] -= 1
            if window_counter[s2[i]] ==0:
                del window_counter[s2[i]]
            if window_counter == counter:
                return True
        return False

        
