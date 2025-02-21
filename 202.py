"""
class Solution:
    def isHappy(self, n: int) -> bool:
        out = set()

        def sum_digits_square(n):
            return (sum([int(y)**2 for y in str(n)]))
        
        z = n
        while sum_digits_square(z) != 1:
            if sum_digits_square(z) not in out:
                out.add(sum_digits_square(z))
                z = sum_digits_square(z)
            else: return False
        
        return True

"""

#using fast and slow pointers
class Solution:
    def isHappy(self, n: int) -> bool:
        def sum_digits_square(n):
            return sum(int(digit) ** 2 for digit in str(n))

        slow, fast = n, sum_digits_square(n)
        while fast != 1 and slow != fast:
            slow = sum_digits_square(slow)  # Moves 1 step
            fast = sum_digits_square(sum_digits_square(fast))  # Moves 2 steps

        return fast == 1
