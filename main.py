class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        l = 0
        j = 0
        i = 0
        while i in range(len(nums)):
            if nums[i] != 1:
                j = 0
            elif nums[i] == 1:
                j += 1
            i += 1
            l = max(l, j)
        return l
