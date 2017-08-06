### Unique Binary Search Trees
Given n, how many structurally unique BST's (binary search trees) that store values 1...n?

For example,
Given n = 3, there are a total of 5 unique BST's.

   1         3     3      2      1
    \       /     /      / \      \
     3     2     1      1   3      2
    /     /       \                 \
   2     1         2                 3

[leetcode](https://leetcode.com/problems/unique-binary-search-trees/description/)

### Answer 
One has a value at the root. the number of method is the combination between left tree and right tree. 

	class Solution {
	public:
	    int numTrees(int n) {
	        vector<int> dp(n + 1, 0);
	        dp[0] = 1;
	        for (int i = 1; i <= n; ++i)
	        {
	            for (int j = 1; j <= i; ++j)
	            {
	                dp[i] += dp[j-1]*dp[i-j];
	            }
	        }
	        
	        return dp[n];
	    }
	};