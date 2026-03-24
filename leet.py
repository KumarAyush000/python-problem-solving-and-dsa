"""
# 1) Remove Duplicates from Dataset
class Solution:
    def removeDuplicates(self, nums: list[int]) -> list[int]:
        uniq_list = []
        for n in nums:
            if n not in uniq_list:
                uniq_list.append(n)
        return uniq_list

lst = Solution()
nums = [5,5,5]
print(lst.removeDuplicates(nums))      
"""
"""
Test case 1
Input: [1, 2, 2, 3, 1, 4]
Output: [1, 2, 3, 4]

Test case 2
Input: [5, 5, 5]
Output: [5]
"""
# 2) Count Frequency of Elements
class Solution:
    def countFrequency(self, nums: list[int]) -> dict:
        element_freq = {}
        for n in nums:
            element_freq[n] = element_freq.get(n, 1)
            if n in element_freq.keys():
                element_freq[n] += 1
        return element_freq

"""
Input: [1, 2, 2, 3]
Output: {1: 1, 2: 2, 3: 1}

Input: []
Output: {}
"""
lst = Solution()
nums = []
print(lst.countFrequency(nums))      




