### Out of Boundary Paths
There is an m by n grid with a ball. Given the start coordinate (i,j) of the ball, you can move the ball to adjacent cell or cross the grid boundary in four directions (up, down, left, right). However, you can at most move N times. Find out the number of paths to move the ball out of grid boundary. The answer may be very large, return it after mod 109 + 7.

Example 1:
Input:m = 2, n = 2, N = 2, i = 0, j = 0
Output: 6
Explanation:

Example 2:
Input:m = 1, n = 3, N = 3, i = 0, j = 1
Output: 12
Explanation:

Note:
Once you move the ball out of boundary, you cannot move it back.
The length and height of the grid is in range [1,50].
N is in range [0,50].

[leetcode](https://leetcode.com/problems/out-of-boundary-paths/description/)

### Answer

It is a dp problem. dp[i][j][k]. means grid[i][j] at k th step the number of path it i j

dp[i][j][k] = dp[i-1][j][k-1] + dp[i+1][j][k-1] + dp[i][j-1][k-1] + dp[i][j+1][k-1]

finally, result = sum over k

	class Solution {
	public:
	    int findPaths(int m, int n, int N, int i, int j) {
	        vector<vector<vector<long>>> dp(N + 1, vector<vector<long>> (m + 2, vector<long> (n + 2, 0)));
	        int factor = 1000000007;
	        ++i;
	        ++j;
	        dp[0][i][j] = 1;
	        for (int iter = 1; iter <= N; ++iter)
	        {
	            for (int r = 0; r <= m + 1; ++r)
	            {
	                for (int c = 0; c <= n + 1; ++c)
	                {
	                    if (r - 1 > 0 && c > 0 && c < n + 1) 
	                        dp[iter][r][c] += dp[iter-1][r-1][c];
	                    if (r + 1 < m + 1 && c > 0 && c < n + 1) 
	                        dp[iter][r][c] += dp[iter-1][r+1][c];
	                    if (c - 1 > 0 && r > 0 && r < m + 1) 
	                        dp[iter][r][c] += dp[iter-1][r][c-1];
	                    if (c + 1 < n + 1 && r > 0 && r < m + 1) 
	                        dp[iter][r][c] += dp[iter-1][r][c+1];
	                    dp[iter][r][c] %= factor;
	                }
	            }
	        }
	        
	        long result = 0;
	        for (int iter = 0; iter <= N; ++iter)
	        {
	            for (int c = 1; c < n + 1; ++c)
	            {
	                result += dp[iter][0][c];
	                result %= factor;
	            }
	                

	            for (int r = 1; r < m + 1; ++r)
	            {
	                result += dp[iter][r][n + 1];
	                result %= factor;
	            }

	            for (int c = n; c > 0; --c)
	            {
	                result += dp[iter][m + 1][c];
	                result %= factor;
	            }

	            for (int r = m; r > 0; --r)
	            {
	                result += dp[iter][r][0];
	                result %= factor;
	            }
	        }
	        
	        return result;
	    }
	};
