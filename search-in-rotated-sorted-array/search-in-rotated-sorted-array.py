class Solution:
    def search(self, nums: List[int], target: int) -> int:
        
        i = 0
        j = len(nums) - 1
        
        # First find the cutoff index
        while nums[i] > nums[j]:
            mid = int((i+j)/2)
            if nums[i] <= nums[mid]:
                i = mid + 1
            else:
                j = mid
                
        #If target falls between the cutoff index and the end
        if nums[i] <= target <= nums[-1]:
            # then we need to search the "tail" of nums
            j = len(nums) - 1
        else:
            # otherwise, we search the "head" of nums
            i = 0
        
        while i < j:
            mid = int((i+j)/2)
            if nums[mid] < target:
                i = mid + 1
            else:
                j = mid
        if nums[i] == target:
            return i
        else:
            return -1