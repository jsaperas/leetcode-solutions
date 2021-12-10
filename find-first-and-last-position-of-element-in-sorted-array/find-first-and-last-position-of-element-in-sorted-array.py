class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
    
        if len(nums) == 0:
            return [-1, -1]
        
        i = 0
        j = len(nums) - 1
        
        while i < j:
            mid = int((j + i)/2)
            if nums[mid] < target:
                i = mid + 1
            else:
                j = mid
                
        if nums[i] == target:
            start_end = [i, -1]
        else:
            return [-1,-1]
        
        j = len(nums) - 1
        while i < j:
            mid = int((j + i)/2) + 1
            if nums[mid] > target:
                j = mid - 1
            else:
                i = mid
                
        if nums[j] == target:
            start_end[1] = j
        
        return start_end
            
            
            
            
            
        
            