

class Solution:
    def getRow(self, rowIndex: int) -> List[List[int]]:
        if rowIndex == 0:
            return [1]
        
        triangle = [[1]]  # Starting with the first row
        
        for row in range(1, rowIndex+1):
            prev_row = triangle[-1]
            current_row = [1]  # Each row starts with 1
            
            # Calculate the middle values
            for i in range(1, len(prev_row)):
                current_row.append(prev_row[i - 1] + prev_row[i])
            
            current_row.append(1)  # Each row ends with 1
            triangle.append(current_row)
        
        return triangle[-1]
