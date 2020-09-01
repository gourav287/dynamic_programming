# -*- coding: utf-8 -*-

"""
Statement:
    Given a matrix M of dimension (m, n) find the minimum value of path to
    traverse from (0, 0) to (m, n) i.e. from top left to bottom right.
    One can only traverse either one step right or one step down, starting
    from (0, 0).
"""

# The solution function
"""
Idea is to use bottom up approach, keep calculating intermediate values
of path starting from bottom down such that minimum value path is chosen.
The path value at the top left index will be the minimum value of traversing
the matrix with given constraints.
"""
def MinPath(matrix, m, n):
    
    # Matrix to store intermediate values
    min_vals = [[0 for i in range(n)] for i in range(m)]
    
    # Temporary variables to store possible cost of moving in both directions
    right, down = 0, 0
    
    # Traversing through the matrix in bottom up fashion
    for col in range(n-1, -1, -1):
        
        for row in range(m - 1, -1, -1):
            
            # Last row, can't move down
            if row == m - 1:
                
                down = 0
            
            else:
                
                down = min_vals[row + 1][col]
            
            # Last column, can't move right
            if col == n - 1:
                
                right = 0
            
            else:
                
                right = min_vals[row][col + 1]
            
            # Update the cost of minimum path when both paths are valid
            if col != n - 1 and row != m - 1:
            
                min_vals[row][col] = matrix[row][col] + min(right, down)
            
            # Update the cost of the valid path as invalid path will 
            # have a zero cost
            else:
                
                min_vals[row][col] = matrix[row][col] + max(right, down)
    
    # Uncomment next 2 lines to print the intermediate value matrix
    
    #for i in range(4):
    #    print(min_vals[i])
    
    # Return the top left element as it contains the required traversal cost
    return min_vals[0][0]

# The driver code
if __name__ == '__main__':
    
    # Input the dimensions of the matrix
    row, col = map(int, input().split())
    
    mine = [list(map(int, input().split())) for i in range(row)]
  
    print("Cost of traversal = {}".format(MinPath(mine, row, col))) 