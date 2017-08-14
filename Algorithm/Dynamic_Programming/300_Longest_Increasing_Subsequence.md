### Longest Increasing Subsequence
Given an unsorted array of integers, find the length of longest increasing subsequence.

For example,
Given [10, 9, 2, 5, 3, 7, 101, 18],
The longest increasing subsequence is [2, 3, 7, 101], therefore the length is 4. Note that there may be more than one LIS combination, it is only necessary for you to return the length.

Your algorithm should run in O(n2) complexity.

Follow up: Could you improve it to O(n log n) time complexity?

[leetcode](https://leetcode.com/problems/longest-increasing-subsequence/description/)

### Answer 

Using DP gives us O(N^2). 

	class Solution {
	public:
	    int lengthOfLIS(vector<int>& nums) {
	        int len = nums.size();
	        vector<int> dp(len, 1);
	        int max_len = 0;
	        for (int i = 0; i < len; ++i)
	        {
	            for (int j = 0; j < i; ++j)
	            {
	                if (nums[j] < nums[i]) dp[i] = max(dp[i], dp[j] + 1);
	            }
	            max_len = max(max_len, dp[i]);
	        }
	        return max_len;
	    }
	};