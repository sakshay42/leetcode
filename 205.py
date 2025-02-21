"""
class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        isomorphism = {}
        for i in range(len(s)):
            if s[i] not in isomorphism and t[i] not in isomorphism.values():
                isomorphism[s[i]] = t[i]
            elif s[i] in isomorphism and isomorphism[s[i]] == t[i]: continue
            else: return False
        return True 
"""


## Lookup in sets take O(1) time
class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        isomorphism = {}
        used_values = set()
        for i in range(len(s)):
            if s[i] not in isomorphism and t[i] not in used_values:
                isomorphism[s[i]] = t[i]
                used_values.add(t[i])
            elif s[i] in isomorphism and isomorphism[s[i]] == t[i]: continue
            else: return False
        return True 
