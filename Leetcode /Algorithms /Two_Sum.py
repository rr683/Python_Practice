class Solution(object):

    def twoSum(self, nums, target):
        """

        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        nums = [2, 5, 7, 11, 15]
        for i in range(len(nums)): # outputs len(nums) -> 5; range(5) -> (0,5)
            for j in range(i+1, len(nums)): #same as above
                if target == nums[i] + nums[j]: #outputs nums[i], nums[j] = *extracts value in array*
                    return target[i,j] #returns duple
