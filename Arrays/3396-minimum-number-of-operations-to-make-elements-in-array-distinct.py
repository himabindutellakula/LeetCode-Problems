class Solution(object):
    def minimumOperations_bruteforce(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if len(nums) == len(set(nums)):
            return 0
        
        unique = False
        cuts = 0
        while(not unique):
            print(nums)
            cuts += 1
            if len(nums) < 3:
                if len(nums) == len(set(nums)):
                    unique = True
                    cuts -= 1
                else:
                    unique = True
            else:
                nums = nums[3:]
                if len(nums) == len(set(nums)):
                    unique = True
        return cuts
        # time complexity of this is O(n*2)
        
        # this can be done in O(n) as below
    
    def minimumOperations(self, nums):
        s = set()
        for i in range(len(nums) - 1, -1, -1):
            if nums[i] in s:
                break
            s.add(nums[i])
        else:
            print(i)
            return 0  # The entire array is already distinct

        x = i + 1  # Number of elements we need to remove from the beginning

        if x % 3 == 0:
            return x // 3
        else:
            return x // 3 + 1  # Round up if not divisible by 3
    
        


                


