from algorithms.strings import StringUtils
from algorithms.arrays import ArrayUtils
from algorithms.dictionaries import DictionaryUtils
from algorithms.recursion import RecursionUtils
from algorithms.data_processing import DataProcessUtils
"""
user_input = StringUtils()
word = input("Enter the word in which you want to count the vowel: ")
print(user_input.vowel_count(word))
"""
"""
user_input = ArrayUtils()
numbers = input("Enter the numbers separated by a comma (,): ")
print(user_input.second_largest(numbers))
"""
"""
user_input = ArrayUtils()
list_input = input("Enter the words separated by a comma (,): ")
print(user_input.duplicate_removal(list_input))
"""
"""
user_input = StringUtils()
word = input("Enter the word you want to reverse: ")
print(user_input.word_reverse(word))
"""
"""
user_input = DictionaryUtils()
word = input("Enter the word: ")
print(user_input.character_frequency(word))
"""
"""
user_input = ArrayUtils()
numbers = input("Enter the numbers separated by a comma (,): ")
print(user_input.missing_number(numbers))
"""
"""
user_input = ArrayUtils()
numbers = input("Enter the numbers separated by a comma (,): ")
print(user_input.missing_number(numbers))
"""
"""
user_input = StringUtils()
word = input("Enter the word to check for palindrome: ")
print(user_input.palindrome_checker(word))
"""
"""
user_input = ArrayUtils()
user_input_list = input("Enter the numbers separated by a comma (,) for the lists and use (/) to separate lists: ")
try:
    print(user_input.common_elements(user_input_list))
except ValueError as e:
    print("Error:", e)
"""
"""
user_input = ArrayUtils()
numbers = input("Enter the numbers separated by a comma (,) to find even and odd count: ")
try:
    print(user_input.even_odd_count(numbers))
except ValueError as e:
    print("Error:",e)
"""
"""
user_input = RecursionUtils()
matrix = input("Enter the elements for the list separated by comma(',') to move to the next nested lsit use('/'): ")
print(user_input.flatten_list(matrix))
"""
"""
user_input = DictionaryUtils()
paragraph = input("Enter the paragraph : ")
print(user_input.word_frequency(paragraph))
"""
"""
user_input = StringUtils()
word1 = input("Enter the first word to check for anagram: ")
word2 = input("Enter the second word to check for anagram: ")
print(f"Anagram: {user_input.anagram_finder(word1, word2)}")
"""
"""
merged_dictionary = DictionaryUtils()
d1 = {'a': 100, 'b': 200, 'c': 300}
d2 = {'a': 300, 'b': 200, 'd': 400}
print(merged_dictionary.merge_dictionaries(d1,d2))
"""
"""
user_input = StringUtils()
word = input("Enter the word: ")
print(user_input.first_non_rep_char(word))
"""
"""
user_input = DataProcessUtils()
json_data = [
    {"name": "Anil", "age": 21},
    {"name": "Ravi", "age": 22}
]
df = user_input.json_dict_to_csv(json_data, "output.csv")
print(df)
"""
"""
user_input = StringUtils()
sentence = input("Enter the sentence: ")
print(user_input.longest_word(sentence))
"""
user_input = ArrayUtils()
nums = input("Enter the numbers separated by a comma (,): ")
k = input("Enter the rotation length: ")
try:
    print(user_input.rotate_list_slicing(nums, k))
except ValueError as e:
    print("Error: ", e)