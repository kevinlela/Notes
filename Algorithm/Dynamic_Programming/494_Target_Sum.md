### Target Sum
You are given a list of non-negative integers, a1, a2, ..., an, and a target, S. Now you have 2 symbols + and -. For each integer, you should choose one from + and - as its new symbol.

Find out how many ways to assign symbols to make sum of integers equal to target S.

Example 1:
Input: nums is [1, 1, 1, 1, 1], S is 3. 
Output: 5
Explanation: 

-1+1+1+1+1 = 3
+1-1+1+1+1 = 3
+1+1-1+1+1 = 3
+1+1+1-1+1 = 3
+1+1+1+1-1 = 3

There are 5 ways to assign symbols to make the sum of nums be target 3.
Note:
The length of the given array is positive and will not exceed 20.
The sum of elements in the given array will not exceed 1000.
Your output answer is guaranteed to be fitted in a 32-bit integer.

[leetcode](https://leetcode.com/problems/target-sum/description/)

### Answer
minus disables dp at the first time thinking. Suppose the array has positive part sum up to P1, and negative part sum up to -P2

we know P1 = S + P2 = S + P - P1

P1 = (S + P)/2

This becomes a dp problem

	class Solution {
	public:
	    int findTargetSumWays(vector<int>& nums, int S) {
	        int sum = 0;
	        for (int i = 0; i < nums.size(); ++i)
	            sum += nums[i];
	        if (S > sum || (S + sum)%2) return 0;
	        int t = (S + sum)/2;
	        int len = nums.size();
	        vector<vector<int>> dp(len + 1, vector<int>(t + 1, 0));
	        dp[0][0] = 1;
	        for (int j = 1; j <= len; j++)
	        {
	            for (int i = 0; i <= t; ++i)
	            {
	                dp[j][i] += dp[j-1][i];
	                if (i - nums[j-1] >= 0) dp[j][i] += dp[j-1][i-nums[j-1]];
	            }
	        }
	        return dp[len][t];
	    }
	};
