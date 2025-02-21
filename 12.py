class Solution:
        """   def intToRoman(self, num: int) -> str:
        dictionary = {"M": 1000, "CM": 900, "D": 500, "CD": 400, "C": 100, "XC": 90, "L": 50, "XL": 40,"X": 10, "IX": 9, "V": 5, "IV": 4,"I": 1}
        
        out = ""
        
        for roman, value in dictionary.items():
            while num >= value:
                out += roman
                num -= value
            
        return out"""

        def intToRoman(self, num: int) -> str:
            dictionary = [("M", 1000), ("CM", 900), ("D", 500), ("CD", 400),("C", 100), ("XC", 90), ("L", 50), ("XL", 40),("X", 10), ("IX", 9), ("V", 5), ("IV", 4),("I", 1) ]
            
            out = ""
            
            for roman, value in dictionary:
                if num == 0:
                    break
                count = num // value
                out += roman * count
                num -= value * count
            
            return out
