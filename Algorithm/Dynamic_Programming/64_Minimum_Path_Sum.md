### Minimum Path Sum
Given a m x n grid filled with non-negative numbers, find a path from top left to bottom right which minimizes the sum of all numbers along its path.

Note: You can only move either down or right at any point in time.

[leetcode](https://leetcode.com/problems/minimum-path-sum/description/)

### Answer 
similar to [62_Unique_Paths.md]
	class Solution {
	public:
	    int minPathSum(vector<vector<int>>& grid) {
	        int m = grid.size();
	        if (m == 0) return 0;
	        int n = grid[0].size();
	        if (n == 0) return 0;
	        
	        vector<vector<int>> dp(m, vector<int> (n, 0));
	        dp[0][0] = grid[0][0];
	        
	        for (int i = 1; i < n; ++i)
	        {
	            dp[0][i] = dp[0][i-1] + grid[0][i];
	        }
	        
	        for (int j = 1; j < m; ++j)
	        {
	            dp[j][0] = dp[j-1][0] + grid[j][0];
	        }
	        
	        for (int j = 1; j < m; ++j)
	        {
	            for (int i = 1; i < n; ++i)
	            {
	                dp[j][i] = min(dp[j-1][i], dp[j][i-1]) + grid[j][i];
	            }
	        }
	        return dp[m-1][n-1];
	    }
	};