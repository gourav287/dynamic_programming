# -*- coding: utf-8 -*-
"""
Given an integer array arr and an arbitrary constant k, find if there exist
a pair (x, y) in the array such that x + y = k.
"""

# The solution code
# Idea is to create a new dictionary that will store the elements that have
# been traced once as keys so that we can compare them with the element being
# traced in O(1) complexity.
# This way we can greatly reduce our time complexity in solving the problem.
def ifSumExist(arr, k):
    
    # The dictionary to store traced elements as keys
    dicti = {}
    
    #Return if the difference exist or else keep appending into the dictionary
    for i in range(len(arr)):
        
        tmp = k - arr[i]
        
        if dicti.get(tmp, 0):
            
            return True
        
        dicti[arr[i]] = 1
    
    # Return False if no pair found
    return False


# The driver code
if __name__ == "__main__":
    
    # Input the array
    arr = list(map(int, input().split()))
    
    # Input the length of array
    k = int(input())
    
    # Check if any two numbers with required sum exist
    if ifSumExist(arr, k):
        
        print("Yes the pair exists in the array !")
    
    else:
        
        print("No such pair exists in the array !")