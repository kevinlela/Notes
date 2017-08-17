### Integer Replacement
Given a positive integer n and you can do operations as follow:

If n is even, replace n with n/2.
If n is odd, you can replace n with either n + 1 or n - 1.
What is the minimum number of replacements needed for n to become 1?

Example 1:

Input:
8

Output:
3

Explanation:
8 -> 4 -> 2 -> 1
Example 2:

Input:
7

Output:
4

Explanation:
7 -> 8 -> 4 -> 2 -> 1
or
7 -> 6 -> 3 -> 2 -> 1

[leetcode](https://leetcode.com/problems/integer-replacement/description/)

### Answer 
It is very lure to think about using dp but n+1 break the dp rule. Actually even use dfs, the complexity is O(2^(log N)) = O(N)

	class Solution {
	public:
	    int integerReplacement(int n) {
	        return recur(n);
	    }
	    
	    int recur(long n)
	    {
	        if (n <= 0) return -1;
	        if (n == 1) return 0;
	        return n % 2 == 0 ? (recur(n/2) + 1 ) : 
	                            (min(recur(n - 1), recur(n + 1)) + 1);
	    }
	};