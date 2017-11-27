### Longest Line of Consecutive One in Matrix
Given a 01 matrix M, find the longest line of consecutive one in the matrix. The line could be horizontal, vertical, diagonal or anti-diagonal.

Example:
Input:
[[0,1,1,0],
 [0,1,1,0],
 [0,0,0,1]]
Output: 3

[leetcode](https://leetcode.com/problems/longest-line-of-consecutive-one-in-matrix/description/)

### Answer

	class Solution {
	public:
	    int longestLine(vector<vector<int>>& M) {
	        int h = M.size();
	        if (h == 0) return 0;
	        int w = M[0].size();
	        if (w == 0) return 0;
	        
	        vector<vector<vector<int>>> dp(h, vector<vector<int>>(w, vector<int>(4, 0)));
	        int result = 0;
	        for (int j = 0, i = 0; j < w; ++j)
	        {
	            if (M[i][j])
	            {
	                dp[i][j][0] = 1;
	                dp[i][j][1] = 1;
	                dp[i][j][2] = 1;
	                dp[i][j][3] = 1;
	                
	                if (j != 0) dp[i][j][0] += dp[i][j-1][0];
	                //cout << dp[i][j][0] << endl;
	                result = max( result, max(max(dp[i][j][0], dp[i][j][1]), max(dp[i][j][2], dp[i][j][3])));
	            }
	        }
	        
	        for (int i = 1; i < h; ++i)
	        {
	            for (int j = 0; j < w; ++j)
	            {
	                if (M[i][j])
	                {
	                    dp[i][j][0] = 1;
	                    dp[i][j][1] = 1;
	                    dp[i][j][2] = 1;
	                    dp[i][j][3] = 1;
	                    
	                    if (j != 0) 
	                    {
	                        dp[i][j][0] += dp[i][j-1][0];
	                        dp[i][j][1] += dp[i-1][j-1][1]; 
	                    }
	                    dp[i][j][2] += dp[i-1][j][2];
	                    if (j != w-1) dp[i][j][3] += dp[i-1][j+1][3] ;
	                    
	                    result = max( result, max(max(dp[i][j][0], dp[i][j][1]), max(dp[i][j][2], dp[i][j][3])));
	                }
	            }
	        }
	                                       
	        return result;                
	    }
	};

