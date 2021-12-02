class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        
        checked = {}
        for i in range(len(nums)):
            remainder = target - nums[i]
            if remainder in checked:
                return [checked[remainder], i]
            else:
                checked[nums[i]] = i
            
                    
        