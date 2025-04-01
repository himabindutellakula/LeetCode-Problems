class Solution(object):
    def maxAbsoluteSum(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        
        #Solved using the kadanes algorithm of maximum subarray
        #Solve that problem first
        maxRes = nums[0]
        minRes = nums[0]
        maxEnd =  nums[0]
        minEnd = nums[0]

        for i in range(1, len(nums)):
            maxEnd = max(maxEnd + nums[i] , nums[i])
            minEnd = min(minEnd + nums[i] , nums[i])
            maxRes = max(maxEnd, maxRes)
            minRes = min(minEnd, minRes)
        
        return max(abs(maxRes), abs(minRes))