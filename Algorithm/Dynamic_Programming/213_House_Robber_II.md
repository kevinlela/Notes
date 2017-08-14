### House Robber II
Note: This is an extension of House Robber.

After robbing those houses on that street, the thief has found himself a new place for his thievery so that he will not get too much attention. This time, all houses at this place are arranged in a circle. That means the first house is the neighbor of the last one. Meanwhile, the security system for these houses remain the same as for those in the previous street.

Given a list of non-negative integers representing the amount of money of each house, determine the maximum amount of money you can rob tonight without alerting the police.

[leetcode](https://leetcode.com/problems/house-robber-ii/description/)

### Answer 
Similar with [198](198_House Robber). Consider two case, steal the last house and not steal the last house. 

	class Solution {
	public:
	    int rob(vector<int>& nums) {
	        // two kinds, can steal the first one, measure to n-2
	        // can not steal the first one, measure to n-2
	        
	        int len = nums.size();
	        if (len == 0) return 0;
	        else if (len == 1) return nums[0];
	        
	        int prev2 = nums[0];
	        int prev1 = max(nums[0], nums[1]);
	        for (int k = 2; k < len - 1; ++k)
	        {
	            int curr = max(prev2 + nums[k], prev1);
	            prev2 = prev1;
	            prev1 = curr;
	        }
	        int res1 = prev1;
	        
	        prev2 = 0;
	        prev1 = nums[1];
	        for (int k = 2; k < len; ++k)
	        {
	            int curr = max(prev2 + nums[k], prev1);
	            prev2 = prev1;
	            prev1 = curr;
	        }
	        
	        return max(res1, prev1);
	    }
	};