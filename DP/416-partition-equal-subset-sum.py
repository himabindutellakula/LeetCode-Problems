class Solution(object):
    def canPartition(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        #we have to divide the entire array into 2 parts with all elements included
        #and no repitition

        #so we need to find subsets with sum = total sum / 2
        #and lets say if we find that array of element with sum one sum/2 is posssible
        #then the answer is yes
        
        if sum(nums) % 2 != 0:
            return False
        
        target = sum(nums) // 2

        dp = [False] * (target+1)
        dp[0] = True

        for num in nums:
            for i in range(target, num-1, -1):
                dp[i] = dp[i-num] or dp[i]
        return dp[target]