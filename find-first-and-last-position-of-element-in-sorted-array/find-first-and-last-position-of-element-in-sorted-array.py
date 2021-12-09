class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        
        start = -1
        end = -1
        i = 0

        while i < len(nums) and end == -1:
            if nums[i] == target and start == -1:
                start = i
                i += 1
            elif nums[i] != target and start != -1:
                end = i-1
            else:
                i += 1
            
        end = i-1 if start != -1 else end
        return [start, end]
            