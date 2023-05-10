from typing import List
import unittest

def spiralOrder(matrix: List[List[int]]) -> List[int]:
    returnList = []
    m = len(matrix) #rows
    n = len(matrix[0]) #columns
    
    if (m == 1):
        return matrix[0]

    top_row = 0; 
    bottom_row = m; 
    left_col = 0; 
    right_col = n 


    c = 0; 
    r = 0; 

    while (top_row < m/2 and left_col < n/2):
        for c in range(left_col, right_col):
            returnList += [matrix[r][c]]
        
        top_row += 1
        for r in range (top_row, bottom_row):
            returnList += [matrix[r][c]]
        
        right_col -= 1
        if (top_row == bottom_row):
            break
        for c in range(right_col-1, left_col-1, -1):
            returnList += [matrix[r][c]]
            
        if (right_col == left_col):
            break
        
        bottom_row -= 1
        for r in range (bottom_row-1, top_row-1,-1):
            returnList += [matrix[r][c]]
        
        left_col += 1
        

    return returnList
#class Test(unittest.TestCase):
#    self.assertEqual(spiralOrder([[1,2,3],[4,5,6],[7,8,9]]), [1,2,3,6,9,8,7,4,5])

if __name__ == "__main__":
    assert spiralOrder( matrix=[[1,2,3],[4,5,6],[7,8,9]]) == [1,2,3,6,9,8,7,4,5]
    
    assert spiralOrder( matrix= [[1,2,3,4],[5,6,7,8],[9,10,11,12]]) == [1,2,3,4,8,12,11,10,9,5,6,7]
    assert spiralOrder(matrix = [[7],[9],[6]]) == [7,9,6]
    
    
