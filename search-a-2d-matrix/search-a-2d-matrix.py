class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        r1 = 0
        r2 = len(matrix) - 1
        n = len(matrix[0]) - 1
        while r1 < r2:
            mid = int((r1 + r2)/2)
            if matrix[mid][n] < target :
                r1 = mid + 1 
            else:
                r2 = mid
                
        if r1 > len(matrix) - 1:
            return False
            
        c1 = 0
        c2 = n
        while c1 < c2:
            mid = int((c1 + c2)/2)
            if matrix[r1][mid] < target:
                c1 = mid + 1
            else:
                c2 = mid
        
        return matrix[r1][c1] == target
        
        
                
        