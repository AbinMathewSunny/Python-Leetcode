from typing import List

class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        if numRows == 0:
            return []
        
        triangle = [[1]]  
        
        for row in range(1, numRows):
            prev_row = triangle[-1]
            current_row = [1]  
            
            for i in range(1, len(prev_row)):
                current_row.append(prev_row[i - 1] + prev_row[i])
            
            current_row.append(1)  
            triangle.append(current_row)
        
        return triangle
