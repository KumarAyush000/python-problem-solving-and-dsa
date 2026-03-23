class StringUtils :
    # vowel counter
    def vowel_count(self, word : str) -> int:
        word = word.strip().lower()
        count = 0
        for w in word:
            if w in "aeiou":
                count+= 1
        return count
    #Reverse word order in a sentence.
    def word_reverse(self,word : str) -> str:
        word = word.strip().lower()
        word = word[::-1]
        return word
    #To check if string is palindrome.
    def palindrome_checker(self, word : str) -> str:
        word = word.strip().lower()
        return word == word[::-1]
    #Group words that are anagrams.
    def anagram_finder(self, word1 : str, word2 : str) -> bool:
        word1 = word1.strip().lower()
        word2 = word2.strip().lower()
        return sorted(word1) == sorted(word2)

