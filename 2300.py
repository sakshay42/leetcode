from collections import defaultdict
class Solution:
    def successfulPairs(self, spells: List[int], potions: List[int], success: int) -> List[int]:
        potions = sorted(potions)

        n = len(potions)
        """def findLeastSuccessfulPotion(strength): #find index of minimum potent potion for a given strength
            min_potency = success/strength
            left = 0
            right = n-1
            while left <= right:
                mid = (left + right) // 2
                if potions[mid] >= min_potency:
                    right = mid-1
                else:
                    left = mid+1
                
            return n-left"""
        
        
        """return [findLeastSuccessfulPotion(strength) for strength in spells]"""
        return [ n-bisect.bisect_left(potions, (success + spell - 1) // spell ) for spell in spells]
        

            
            

        
