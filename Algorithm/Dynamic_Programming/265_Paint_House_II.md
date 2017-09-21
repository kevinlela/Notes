### Paint House II
There are a row of n houses, each house can be painted with one of the k colors. The cost of painting each house with a certain color is different. You have to paint all the houses such that no two adjacent houses have the same color.

The cost of painting each house with a certain color is represented by a n x k cost matrix. For example, costs[0][0] is the cost of painting house 0 with color 0; costs[1][2] is the cost of painting house 1 with color 2, and so on... Find the minimum cost to paint all houses.

Note:
All costs are positive integers.

Follow up:
Could you solve it in O(nk) runtime?

[leetcode](https://leetcode.com/problems/paint-house-ii/description/)

### Answer
* to use dp, the simplest solution is O(nk^2) because every time we need to go back to find the minimum
* but actually, the minimum can be calculate for each row only once
* there are two situation, the element in the next row with the same color as the one in the previous row with the minimum cost -> we need to store the secound smallest. second, if not same color, we can just use the one. 
	class Solution {
	public:
	    int minCostII(vector<vector<int>>& costs) {
	        int n = costs.size();
	        if (n == 0) return 0;
	        int k = costs[0].size();
	        if (k == 0) return -1;
	        if (k == 1 && n > 1) return -1;
	        
	        vector<vector<int>> dp(n, vector<int>(k, 0));
	        int min1 = INT_MAX, min2 = INT_MAX;
	        for (int j = 0; j < k; ++j)
	        {
	            dp[0][j] = costs[0][j];
	            if (dp[0][j] < min1)
	            {
	                min2 = min1;
	                min1 = dp[0][j];
	            }
	            else if (dp[0][j] < min2) min2 = dp[0][j];
	        }
	        
	        for (int i = 1; i < n; ++i)
	        {
	            int min1_tmp = INT_MAX, min2_tmp = INT_MAX;
	            for (int j = 0; j < k; ++j)
	            {
	                if (dp[i-1][j] == min1) dp[i][j] = min2 + costs[i][j];
	                else dp[i][j] = min1 + costs[i][j];
	                if (dp[i][j] < min1_tmp)
	                {
	                    min2_tmp = min1_tmp;
	                    min1_tmp = dp[i][j];
	                }
	                else if (dp[i][j] < min2_tmp) min2_tmp = dp[i][j];
	            }
	            min1 = min1_tmp;
	            min2 = min2_tmp;
	        }
	        
	        int result = INT_MAX;
	        for (int j = 0; j < k; ++j)
	            result = min(result, dp[n-1][j]);
	            
	        return result;
	    }
	};