class Solution(object):
    def threeSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        empty_list = []
        if len(nums) < 3:
            return []
        else:
            empty_list.append(nums[0])
            for i in range(1, len(nums)):
                if nums[i] != empty_list[i - 1]:
                    empty_list.append(nums)


sol = Solution()
print(sol.threeSum([1, 3, 4]))
