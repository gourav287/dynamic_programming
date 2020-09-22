/*
Longest Palindromic Subsequence :
Given a String, find the longest palindromic subsequence

The problem is solved in C++ as python was proving to be slow language in the case of this problem,
Dynamic programming has been used and the time complexity has been brought down to O(n*n)
*/

// Including necessary library
#include <iostream>
#include <bits/stdc++.h> 
using namespace std;

// Function to get the max of two elements
int max(int a,int b) {return a >= b ? a : b;}

// The function to calculate longest common subsequence
int lcs(string s, string rs)
{
    // Initialize i, j and Length of string
    int i, j, leng = s.length();
    
    // Working with the dynamic programming
    int arr[leng+1][leng+1];
    for (i=0;i<=leng;i++)
        for(j=0;j<=leng;j++)
            arr[i][j] = 0;
    
    /* Build the table. Note that there are multiple cases which are
    covered using if-else blocks.
    */
    for(i=1;i<=leng;i++)
    {
        for(j=1;j<=leng;j++)
        {
            //Indexing from 1
            if (i==0 || j==0)
            {
                arr[i][j] = 0;
            }
            
            // If both the letters match, this is the part of palindromic subsequence
            if (s[i-1] == rs[j-1])
            {
                arr[i][j] = arr[i-1][j-1] + 1;
            }
            
            // Else keep traversing with the maximum seen length of the subsequence.
            else
            {
                arr[i][j] = max(arr[i-1][j], arr[i][j-1]);
            }
        }
    }
    // last element has the value of longest palindromic subsequence 
    return arr[leng][leng];
}

// The driver code
int main() {
    
	int n, i;
	
	// No of test cases
	cin >> n;
	
	for(i=0;i<n;i++)
	{
	    // longest common subsequence of a string and its reverse will always be the
	    // longest palindromic subsequence
	    string s;
	    cin >> s;
	    string rs = s;
	    reverse(rs.begin(), rs.end());
	    cout << lcs(s, rs) << endl;
	}
	return 0;
}