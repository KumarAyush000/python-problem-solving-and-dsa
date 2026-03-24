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
    #Merge dictionaries and sum common keys.
    # approach1: to show logic
    """
    def merge_dictionaries(self, dic1: dict, dic2: dict) -> dict:
         merged_dict = dict.copy()
         for key, value in dic2.items():
              merged_dict[key] = merged_dict.get(key, 0) + value
         return merged_dict
    """
    # approach2: using counter
    def merge_dictionaries(self, dic1: dict, dic2: dict) -> dict:
         from collections import Counter
         merged_dict = Counter(dic1) + Counter(dic2)
         return dict(merged_dict)
        

        


        