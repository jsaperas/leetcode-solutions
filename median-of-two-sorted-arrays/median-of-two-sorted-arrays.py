class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        
        # Merge both lists in order
        i = 0
        j = 0
        combined = []

        while i < len(nums1) and j < len(nums2):
            if nums1[i] < nums2[j]:
                combined.append(nums1[i])
                i += 1
            else:
                combined.append(nums2[j])
                j += 1
        
        # Append any remaining numbers from either list
        combined.extend(nums1[i:])
        combined.extend(nums2[j:])
        
        # Calculate median
        index = int(len(combined) / 2)
        if len(combined) % 2 == 0:
            median = (combined[index-1] + combined[index]) / 2
        else:
            median = combined[index]
            
        return median
