class Solution(object):
    def minOperations(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        setNums = set(nums)
        minimum = min(nums)
        if minimum < k:
            return -1
        elif minimum == k:
            return len(setNums) - 1
        return len(setNums)

        #answer is no of distinct integers in array that are greater than k
        