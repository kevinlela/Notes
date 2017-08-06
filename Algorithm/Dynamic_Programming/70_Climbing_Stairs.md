### Climbing Stairs
You are climbing a stair case. It takes n steps to reach to the top.

Each time you can either climb 1 or 2 steps. In how many distinct ways can you climb to the top?

Note: Given n will be a positive integer.

[leetcode](https://leetcode.com/problems/climbing-stairs/description/)

### Answer 
the current status dp[i] only comes from dp[i-1] and dp[i-2]

	class Solution {
	public:
	    int climbStairs(int n) {
	        if (n <= 1) return 1;
	        int prev_2 = 1, prev_1 = 1;
	        
	        for (int i = 2; i <= n; ++i)
	        {
	            int curr = prev_2 + prev_1;
	            prev_2 = prev_1;
	            prev_1 = curr;
	        }
	        
	        return prev_1;
	    }
	};