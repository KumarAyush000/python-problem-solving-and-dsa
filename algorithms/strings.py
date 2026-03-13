# vowel counter
class StringUtils :
    def vowel_count(self, word):
        word = word.strip().lower()
        count = 0

        for w in word:
            if w in "aeiou":
                count+= 1

        return count

       

