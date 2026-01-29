"""
Day 01 - Two Sum (LeetCode 1)

AIDD Mapping:
Fragment / fingerprint hash lookup

Key Data Structure:
Dict (Hash Table)

Goal:
Given an integer array and a target, find two indices such that their sum equals target.
"""

from typing import List

class Solution:
	def twoSumbruteforce(self, nums: List[int], target: int) -> List[int]:
		for i in range(len(nums)):           #找第一个数位置
			for j in range(i+1, len(nums)):   #找第二个数位置
				if nums[i] +nums[j] == target:
					return [i, j]


	def twoSumhash(self, nums: List[int], target: int) -> List[int]:
		hashmap = {}   #定义字典，存储记忆
		for i, num in enumerate(nums):   #核心函数
			need = target-num
			if need in hashmap:
				return [hashmap[need], i] #返回之前那个数的下标与当前数的下标
			hashmap[num] = i  #当前数加入记忆