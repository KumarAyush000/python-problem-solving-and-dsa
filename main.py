from algorithms.strings import StringUtils
from algorithms.arrays import ArrayUtils
from algorithms.dictionaries import DictionaryUtils
from algorithms.recursion import RecursionUtils
from algorithms.data_processing import DataProcessUtils
"""
#DAY 1
user_input = StringUtils()
word = input("Enter the word in which you want to count the vowel: ")
print(user_input.vowel_count(word))
"""
"""
#DAY 2
user_input = ArrayUtils()
numbers = input("Enter the numbers separated by a comma (,): ")
print(user_input.second_largest(numbers))
"""
"""
#DAY 3
user_input = ArrayUtils()
list_input = input("Enter the words separated by a comma (,): ")
print(user_input.duplicate_removal(list_input))
"""
"""
#DAY 4
user_input = StringUtils()
word = input("Enter the word you want to reverse: ")
print(user_input.word_reverse(word))
"""
"""
#DAY 5
user_input = DictionaryUtils()
word = input("Enter the word: ")
print(user_input.character_frequency(word))
"""
"""
#DAY 6
user_input = ArrayUtils()
numbers = input("Enter the numbers separated by a comma (,): ")
print(user_input.missing_number(numbers))
"""
"""
#DAY 7
user_input = StringUtils()
word = input("Enter the word to check for palindrome: ")
print(user_input.palindrome_checker(word))
"""
"""
#DAY 8
user_input = ArrayUtils()
user_input_list = input("Enter the numbers separated by a comma (,) for the lists and use (/) to separate lists: ")
try:
    print(user_input.common_elements(user_input_list))
except ValueError as e:
    print("Error:", e)
"""
"""
#DAY 9
user_input = ArrayUtils()
numbers = input("Enter the numbers separated by a comma (,) to find even and odd count: ")
try:
    print(user_input.even_odd_count(numbers))
except ValueError as e:
    print("Error:",e)
"""
"""
#DAY 10
user_input = RecursionUtils()
matrix = input("Enter the elements for the list separated by comma(',') to move to the next nested lsit use('/'): ")
print(user_input.flatten_list(matrix))
"""
"""
#DAY 11
user_input = DictionaryUtils()
paragraph = input("Enter the paragraph : ")
print(user_input.word_frequency(paragraph))
"""
"""
#DAY 12
user_input = StringUtils()
word1 = input("Enter the first word to check for anagram: ")
word2 = input("Enter the second word to check for anagram: ")
print(f"Anagram: {user_input.anagram_finder(word1, word2)}")
"""
"""
#DAY 13
merged_dictionary = DictionaryUtils()
d1 = {'a': 100, 'b': 200, 'c': 300}
d2 = {'a': 300, 'b': 200, 'd': 400}
print(merged_dictionary.merge_dictionaries(d1,d2))
"""
"""
#DAY 14
user_input = StringUtils()
word = input("Enter the word: ")
print(user_input.first_non_rep_char(word))
"""
"""
#DAY 15
user_input = DataProcessUtils()
json_data = [
    {"name": "Anil", "age": 21},
    {"name": "Ravi", "age": 22}
]
df = user_input.json_dict_to_csv(json_data, "output.csv")
print(df)
"""
"""
#DAY 16
user_input = StringUtils()
sentence = input("Enter the sentence: ")
print(user_input.longest_word(sentence))
"""
"""
#DAY 17
user_input = ArrayUtils()
nums = input("Enter the numbers separated by a comma (,): ")
k = input("Enter the rotation length: ")
try:
    print(user_input.rotate_list_slicing(nums, k))
except ValueError as e:
    print("Error: ", e)
"""