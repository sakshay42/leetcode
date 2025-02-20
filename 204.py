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

"""
Python
class Solution(object):
    def countPrimes(self, n):
        if n < 2:
            return 0
        is_prime = bytearray([1]) * n
        is_prime[0] = is_prime[1] = 0  
        for i in range(2, int(n ** 0.5) + 1):
            if is_prime[i]:
                is_prime[i * i:n:i] = bytearray((n - i * i - 1) // i + 1)
        return sum(is_prime)
""""
