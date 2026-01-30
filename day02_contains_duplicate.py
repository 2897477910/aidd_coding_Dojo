#给你一个整数数组 nums 。如果任一值在数组中出现 至少两次 ，返回 true ；如果数组中每个元素互不相同，返回 false 。


from typing import List

class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        """
        思路：哈希表
        使用 set 判断是否出现重复元素
        时间复杂度：O(n)
        空间复杂度：O(n)
        """
        seen = set()
        for x in nums:
            if x in seen:
                return True
            seen.add(x)
        return False
    
"""
    gpt思路：set 判重（时间 & 空间最优解之一）

核心思想
集合（set）只保存唯一元素：

若长度变短 → 有重复
"""

class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        return len(nums) != len(set(nums))
