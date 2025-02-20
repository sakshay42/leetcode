class Solution(object):
    def countPrimes(self, n):
        """
        :type n: int
        :rtype: int
        """
        if n<2: return 0
        sieve = [1]*n
        for i in range(2,n+1):
            if i**2 > n: break
            for j in range(i**2,n,i):
                sieve[j] =0
        return sum(sieve)-2
