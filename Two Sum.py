"""
Given an array of integers nums and an integer target, return indices of the two numbers such that they add up to target.

You may assume that each input would have exactly one solution, and you may not use the same element twice.
"""

class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        index_1 = 0
        while True:
            for index_2 in range(index_1+1, len(nums)):
                if nums[index_1] == target - nums[index_2]:
                    return [index_1, index_2]
            index_1 += 1
