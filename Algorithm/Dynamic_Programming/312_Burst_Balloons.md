### Burst Balloons
Given n balloons, indexed from 0 to n-1. Each balloon is painted with a number on it represented by array nums. You are asked to burst all the balloons. If the you burst balloon i you will get nums[left] * nums[i] * nums[right] coins. Here left and right are adjacent indices of i. After the burst, the left and right then becomes adjacent.

Find the maximum coins you can collect by bursting the balloons wisely.

Note: 
(1) You may imagine nums[-1] = nums[n] = 1. They are not real therefore you can not burst them.
(2) 0 ≤ n ≤ 500, 0 ≤ nums[i] ≤ 100

Example:

Given [3, 1, 5, 8]

Return 167

    nums = [3,1,5,8] --> [3,5,8] -->   [3,8]   -->  [8]  --> []
   	coins =  3*1*5      +  3*5*8    +  1*3*8      + 1*8*1   = 167

[leetcode](https://leetcode.com/problems/burst-balloons/description/)

### Answer 
This is a very hard dp. The final score depends on the last element. because, the left part and right part can be determined if we fixed the last element. 

	class Solution {
	public:
	    int maxCoins(vector<int>& nums) {
	        // this problem, two thoughts may happen
	        // first, I may consider to use greedy algorithm to find out if there is an appearent optimal
	        // strategy but it will fail
	        // then it is about dp algorithm , to solve a dp problem, we need to find an invariant status
	        // in which status, we can borrow the info from previous status?
	        // when x is last poped item, then, the left of x is depending on x and the right of x is also depending on x. 
	        
	        int len = nums.size();
	        if (len == 0) return 0;
	        
	        vector<vector<int>> dp(len, vector<int>(len, 0));
	        
	        for (int i = 0; i < len; ++i)
	        {
	            int lft = i - 1 <    0 ? 1 : nums[i-1];
	            int rgt = i + 1 >= len ? 1 : nums[i+1];
	            dp[i][i] = nums[i]*lft*rgt;
	        }
	        
	        for (int k = 1; k < len; ++k)
	        {
	            for (int j = 0; j < len - k; ++j)
	            {
	                // candidate from [j....j+k]
	                int st = j, ed = j + k;
	                for (int i = st; i <= ed; ++i)
	                {
	                    // dp[j][j+k] means the max score we can get from [j ... j + k]
	                    int last = nums[i];
	                    int lft    = st - 1 <    0 ? 1 : nums[st - 1];
	                    int rgt    = ed + 1 >= len ? 1 : nums[ed + 1];
	                    int lft_dp = i - 1  <   st ? 0 : dp[st][i - 1];
	                    int rgt_dp = i + 1  >   ed ? 0 : dp[i + 1][ed];
	                    
	                    dp[st][ed] = max(dp[st][ed], last * lft * rgt + lft_dp + rgt_dp);
	                }
	            }
	        }
	        
	        return dp[0][len-1];
	    }
	};