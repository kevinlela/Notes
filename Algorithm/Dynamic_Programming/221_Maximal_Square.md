### Maximal Square
Given a 2D binary matrix filled with 0's and 1's, find the largest square containing only 1's and return its area.

For example, given the following matrix:

1 0 1 0 0
1 0 1 1 1
1 1 1 1 1
1 0 0 1 0
Return 4.

[leetcode](https://leetcode.com/problems/maximal-square/description/)

### Answer 

This is a dp problem. let dp[i][j] be the maximal square in matrix [0][0] - [i][j]. it comes from min(dp[i-1][j-1], dp[i-1][j], dp[i][j-1]) + 1. 

It is because the new square must comes from the overlap of these three region. 

	class Solution {
	public:
	    int maximalSquare(vector<vector<char>>& matrix) {
	        int h = matrix.size();
	        if (h == 0) return 0;
	        int w = matrix[0].size();
	        if (w == 0) return 0;
	        
	        vector<vector<int>> dp(h, vector<int> (w, 0));
	        
	        int result = 0;
	        
	        for (int j = 0; j < h; ++j)
	        {
	            dp[j][0] = matrix[j][0] == '1' ? 1 : 0;
	            result = max(result, dp[j][0]);
	        }
	        
	        for (int i = 0; i < w; ++i)
	        {
	            dp[0][i] = matrix[0][i] == '1' ? 1 : 0;
	            result = max(result, dp[0][i]);
	        }
	        
	        
	        for (int j = 1; j < h; ++j)
	        {
	            for (int i = 1; i < w; ++i)
	            {
	                dp[j][i] = matrix[j][i] == '0' ? 0 : 
	                    (min(dp[j-1][i-1], min(dp[j-1][i], dp[j][i-1]))) + 1;
	            
	                result = max(result, dp[j][i]);
	            }
	        }
	        
	        return result * result;
	    }
	};