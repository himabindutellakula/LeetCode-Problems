class Solution(object):
    def maximumTripletValue(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        triplets = set()
        for i in range(len(nums)-2):
            for j in range(i+1, len(nums)-1):
                for k in range(j+1, len(nums)):
                    triplets.add((i, j, k))

        ans = 0
        for i,j,k in triplets:
            ans = max(ans, (nums[i] - nums[j])*nums[k])
        return ans
        #time complexity O(n*3) for generating triplets