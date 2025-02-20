class Solution(object):
    def groupAnagrams(self, strs):
        """
        :type strs: List[str]
        :rtype: List[List[str]]
        """
        out ={}
        for word in strs:
            main_word = tuple(sorted(word))
            if main_word in out:
               out[main_word].append(word)  
            else:
                out[main_word] = [word]

        return list(out.values())
