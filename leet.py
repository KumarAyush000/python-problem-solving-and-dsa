"""
# 1) Remove Duplicates from Dataset
class Solution:
    def removeDuplicates(self, nums: list[int]) -> list[int]:
        uniq_list = []
        for n in nums:
            if n not in uniq_list:
                uniq_list.append(n)
        return uniq_list
"""
# 2) Count Frequency of Elements
class Solution:
    def countFrequency(self, nums: list[int]) -> dict:
        element_freq = {}
        for n in nums:
            element_freq[n] = element_freq.get(n, 0) + 1
        return element_freq



