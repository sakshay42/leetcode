class Solution:
    def wordPattern(self, pattern: str, s: str) -> bool:
        words = s.split()
        isomorphism = {}
        used_values = set()
        print(words)
        if len(pattern)!= len(words):return False
        for i in range(len(pattern)):
            print(isomorphism)
            if pattern[i] not in isomorphism and words[i] not in used_values:
                isomorphism[pattern[i]] = words[i]
                used_values.add(words[i])
            elif pattern[i] in isomorphism and isomorphism[pattern[i]] ==words[i]: continue
            else: return False
        print(isomorphism)
        return True 
            
