# -*- coding: utf-8 -*-
"""
Question link:
    https://practice.geeksforgeeks.org/problems/count-of-strings-that-can-be-formed-using-a-b-and-c-under-given-constraints/0/?category[]=Dynamic%20Programming&company[]=Amazon&company[]=Goldman%20Sachs&problemStatus=unsolved&difficulty[]=0&page=1&query=category[]Dynamic%20Programmingcompany[]Amazoncompany[]Goldman%20SachsproblemStatusunsolveddifficulty[]0page1

Given a length n, count the number of strings of length n that can be made 
using ‘a’, ‘b’ and ‘c’ with at-most one ‘b’ and two ‘c’s allowed.

Input:
2
1
3

Output:
3
19

Explanation:
Test Case 1: N = 1
Possible strings are: "a", "b" and "c"

Test Case 2: N = 3
Number of strings with 3 occurrances of a: 1
2-a and 1-b: 3
2-a and 1-c: 3
1-a, 1-b and 1-c: 6
1-a and 2-c: 3
1-b and 2-c: 3
Hence, total number of strings of length 3 = 1 + 3 + 3 + 6 + 3 + 3 = 19
"""

"""
The question looks like a tricky one from Dynamic Programming, but actually 
is a simple mathematics question where you need to apply Permutation and Combination
Consider all the 6 different scenarios of occurance (b, c) :  {(0, 0), (0, 1), 
(0, 2), (1, 0), (1, 1), (1, 2)}and calculate their permutation values.
Here's the solution in O(1) complexity.
"""

# The driver code
if __name__ == "__main__":
	
	# No of test cases
    for _ in range(int(input())):
        
        # Input the length of number
        n = int(input())
        
        # Formula after solving the math
        val = (n**3 + 3*n)//2 + 1
        
        # print the value
        print(val)
        

"""
NOTE ->
The formula will be :
    fact(n)/fact(n) + fact(n)/fact(n-1) + fact(n)/(fact(n-2)*fact(2))
     + fact(n)/fact(n-1) + fact(n)/fact(n-2) + fact(n)/(fact(n-3)*fact(2))
     
     where fact(n) denotes the factorial of n.
"""