### House Robber
You are a professional robber planning to rob houses along a street. Each house has a certain amount of money stashed, the only constraint stopping you from robbing each of them is that adjacent houses have security system connected and it will automatically contact the police if two adjacent houses were broken into on the same night.

Given a list of non-negative integers representing the amount of money of each house, determine the maximum amount of money you can rob tonight without alerting the police.

[leetcode](https://leetcode.com/problems/house-robber/description/)

### Answer 

every house has two possibility, steal or not steal
* steal : come from i - 2
* not steal : come from i - 1

	class Solution {
	public:
	    int rob(vector<int>& nums) {
	        int len = nums.size();
	        if (len == 0) return 0;
	        if (len == 1) return nums[0];
	        
	        int prev1 = max(nums[1], nums[0]), prev2 = nums[0];
	        
	        for (int k = 2; k < len; ++k)
	        {
	            int curr = max(prev1, nums[k] + prev2);
	            prev2 = prev1;
	            prev1 = curr;
	        }
	        
	        return max(prev2, prev1);
	    }
	};