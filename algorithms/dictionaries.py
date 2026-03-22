class DictionaryUtils:
    #Return frequency of characters in string.
    def character_frequency(self,word : str) -> dict:
        frequency_count = dict.fromkeys(word,0)
        for char in word:
            frequency_count[char] += 1

        return frequency_count
    #Count word frequency in paragraph.
    def word_frequency(self, paragraph : str) -> dict:
            paragraph = paragraph.lower().split()
            word_and_count = {}
            for word in paragraph:
                word = word.strip(",.!?/'-+=*&%$#@")
                if word:
                    word_and_count[word] = word_and_count.get(word, 0) + 1
            return word_and_count
        

        


        