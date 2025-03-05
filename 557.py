class Solution:
    def reverseWords(self, s: str) -> str:
        """
        def reverseword(word):
            left=0
            right = len(word)-1
            word_list = list(word)
            while left < right:
                    word_list[left],word_list[right] = word_list[right],word_list[left]
                    left +=1
                    right -=1

            return "".join(word_list)
        """
        
        words= s.split()
        reversed_words = reverse_words = [word[::-1] for word in words] ###map(reverseword,words)

        return (" ".join(reversed_words))
