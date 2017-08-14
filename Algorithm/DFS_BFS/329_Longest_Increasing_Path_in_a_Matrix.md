###  Longest Increasing Path in a Matrix
Given an integer matrix, find the length of the longest increasing path.

From each cell, you can either move to four directions: left, right, up or down. You may NOT move diagonally or move outside of the boundary (i.e. wrap-around is not allowed).

Example 1:

nums = [
  [9,9,4],
  [6,6,8],
  [2,1,1]
]
Return 4
The longest increasing path is [1, 2, 6, 9].

Example 2:

nums = [
  [3,4,5],
  [3,2,6],
  [2,2,1]
]
Return 4
The longest increasing path is [3, 4, 5, 6]. Moving diagonally is not allowed.

[leetcode](https://leetcode.com/problems/longest-increasing-path-in-a-matrix/description/)

### Answer 
DFS with memorization. We can know a node's longest path whenever visite again. 

	class Solution {
	public:
	    int longestIncreasingPath(vector<vector<int>>& matrix) {
	        int h = matrix.size();
	        if (h == 0) return 0;
	        int w = matrix[0].size();
	        if (w == 0) return 0;
	        
	        vector<vector<int>> dp(h, vector<int> (w, 0));
	        
	        int path = 0;
	        for (int j = 0; j < h; ++j)
	        {
	            for (int i = 0; i < w; ++i)
	            {
	                path = max(path, dfs(matrix, dp, j, i));
	            }
	        }
	        
	        return path;
	    }
	    
	    int dfs(const vector<vector<int>>& matrix, vector<vector<int>> &dp, int j, int i)
	    {
	        int h = matrix.size();
	        int w = matrix[0].size();
	        if (dp[j][i] != 0) return dp[j][i];
	        
	        int curr_path = 0;
	        if (j - 1 >= 0 && matrix[j-1][i] > matrix[j][i]) curr_path = max(curr_path, dfs(matrix, dp, j-1, i));
	        if (j + 1 <  h && matrix[j+1][i] > matrix[j][i]) curr_path = max(curr_path, dfs(matrix, dp, j+1, i));
	        if (i - 1 >= 0 && matrix[j][i-1] > matrix[j][i]) curr_path = max(curr_path, dfs(matrix, dp, j, i-1));
	        if (i + 1 <  w && matrix[j][i+1] > matrix[j][i]) curr_path = max(curr_path, dfs(matrix, dp, j, i+1));
	        
	        dp[j][i] = 1 + curr_path;
	        return dp[j][i];
	    }
	};