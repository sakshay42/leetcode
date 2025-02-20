class Solution(object):
    def maxNumberOfBalloons(self, text):
        """
        :type text: str
        :rtype: int
        """
        chars = {'b': 0, 'a':0, "l": 0, 'o':0, "n":0}
        for i in text:
            if i in chars:
                chars[i] +=1
        chars["l"] //=2
        chars["o"] //=2
        return (min(chars.values()))
