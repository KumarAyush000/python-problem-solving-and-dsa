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
    #Find first non repeating character.
    #Approach 1 (Basic): Time complexity :- O(n^2) 
    # Count takes O(n) ->  Inside a loop O(n^2)
    # --> "Avoid repeated .count() inside loops"
    """
    def first_non_rep_char(self, word: str) -> str | None:
        word = word.strip().lower()
        for w in word:
            if word.count(w) == 1:
                return w
        return None
    """
    #Approach 2 (Optimized): Time complexity :- O(n)
    # Using a dictionary
    def first_non_rep_char(self, word: str) -> str | None:
        word = word.strip().lower()
        freq = {}
        for ch in word:
            freq[ch] = freq.get(ch, 0) + 1
        for ch in word:
            if freq[ch] == 1:
                return ch
        return None
    #Return longest word in sentence.
    def longest_word(self, sentence: str) -> str | None:
        words = [
            word.strip(" ,.!?/'-+=*&%$#@").lower()
            for word in sentence.split()
                ]
        words = [word for word in words if word]
        if not words:
            return None
        longest = words[0]
        for word in words:
            if len(word) > len(longest):
                longest = word

        return longest



