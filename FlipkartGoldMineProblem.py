# -*- coding: utf-8 -*-
# Question Link:
# https://practice.geeksforgeeks.org/problems/gold-mine-problem/0
"""
Statement:
    Given a gold mine (M) of n*m dimensions. Each field in this mine contains 
    a positive integer which is the amount of gold in tons. 
    Initially the miner is at first column but can be at any row.
    From a given cell, the miner can move to the cell diagonally up towards 
    the right or right or diagonally down towards the right. Your task is 
    to find out maximum amount of gold which he can collect.
"""

# The solution function
def GoldCollection(mine, m, n):
    
    # Create a table for storing intermediate values of gold
    m_vals = [[0 for i in range(n)] for i in range(m)]
    
    # Gold collected by the three possible moves
    right, right_up, right_down = 0, 0, 0
    
    # Traverse from right to left, up to down
    # Update the collection from 3 possible moves
    # Update the maximum collection possible
    for j in range(n - 1, -1, -1):
        
        for i in range(m):
            
            # Update right up if going right up is possible
            if i == 0 or j == n-1:
                
                right_up = 0
            
            else:
                
                right_up = m_vals[i - 1][j + 1]
            
            # Update right if going right is possible
            if j == n - 1:
                
                right = 0
            
            else:
                
                right = m_vals[i][j + 1]
            
            # Update right down if going right down is possible
            if i == m - 1 or j == n - 1:
                
                right_down = 0
            
            else:
                
                right_down = m_vals[i + 1][j + 1]
            
            # Update intermediate values
            m_vals[i][j] = mine[i][j] + max(right, right_up, right_down)
    
    # Hence the maximum collection will be stored in the 1st column
    # The row value of maximum collection will tell us where the miner
    # should start from
    max_ = m_vals[0][0]
    
    for i in range(m):
        
        max_ = max(max_, m_vals[i][0])
        
    # Return the maximum collection possible
    return max_

# The driver code
if __name__ == '__main__':
    
    # Dimensions of the mine
    m, n = map(int, input().split())
    
    mine = []
    
    # Input the values of matrix
    for i in range(m):
        
        mine.append(list(map(int, input().split())))
    
    # Print the maximum amount of gold the miner can take
    print(GoldCollection(mine, m, n))