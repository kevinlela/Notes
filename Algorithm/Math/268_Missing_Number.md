### Missing Number
Given an array containing n distinct numbers taken from 0, 1, 2, ..., n, find the one that is missing from the array.

For example,
Given nums = [0, 1, 3] return 2.

Note:
Your algorithm should run in linear runtime complexity. Could you implement it using only constant extra space complexity?

[leetcode](https://leetcode.com/problems/missing-number/description/)

### Answer 
Sum equation

	class Solution {
	public:
	    int missingNumber(vector<int>& nums) {
	        long len = nums.size();
	        long sum = 0;
	        for (int i = 0; i < len; ++i)
	        {
	            sum += nums[i];
	        }
	        return len*(len+1)/2 - sum;
	    }
	};