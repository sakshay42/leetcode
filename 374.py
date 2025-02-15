# The guess API is already defined for you.
# @param num, your guess
# @return -1 if num is higher than the picked number
#          1 if num is lower than the picked number
#          otherwise return 0
# def guess(num: int) -> int:

class Solution:
    def guessNumber(self, n: int) -> int:
        left = 1
        right = n
        while left <= right:
            middle= (left + right)//2
            guessed = guess(middle)
            if guessed==0: return(middle)
            elif guessed ==1: left = middle + 1
            else: right = middle -1
        
