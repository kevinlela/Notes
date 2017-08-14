### Integer Break
Given a positive integer n, break it into the sum of at least two positive integers and maximize the product of those integers. Return the maximum product you can get.

For example, given n = 2, return 1 (2 = 1 + 1); given n = 10, return 36 (10 = 3 + 3 + 4).

Note: You may assume that n is not less than 2 and not larger than 58.

[leetcode](https://leetcode.com/problems/integer-break/description/)

### Answer 
only 2 and 3 has product smaller than itself, So, dp[i] = max(dp[i-2]*2, dp[i-3]*3)

	class Solution {
	public:
	    int integerBreak(int n) {
	        
	        if (n == 2) return 1;
	        if (n == 3) return 2;
	        
	        int v1 = 3, v2 = 2, v3 = 1;
	        
	        for (int i = 4; i <= n; ++i)
	        {
	            int tmp = max(v2*2, v3*3);
	            v3 = v2;
	            v2 = v1;
	            v1 = tmp;
	        }
	        
	        return v1;
	    }
	};