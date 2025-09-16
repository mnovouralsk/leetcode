class Solution(object):
    def search(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        left = 0
        right = len(nums) - 1
        while left <= right:
            midle = (left + right) // 2
            if nums[midle] < target:
                left = midle + 1
            elif nums[midle] > target:
                right = midle - 1
            else:
                return midle
        return -1
