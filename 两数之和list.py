class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        for i in range(len(nums)):
            for j in range(i+1, len(nums)):
                if nums[j] == target - nums[i]:
                    return i, j

    def twoSum2(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        for i in range(len(nums)):
            value = target - nums[i]
            if value in nums and i != nums.index(value):
                return i, nums.index(value)


if __name__ == "__main__":
    aa = Solution()
    nums = [2, 7, 11, 15]
    target = 9
    aa.twoSum(nums, target)
    aa.twoSum2(nums, target)
