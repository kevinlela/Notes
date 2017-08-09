### Single Number
Given an array of integers, every element appears twice except for one. Find that single one.

Note:
Your algorithm should have a linear runtime complexity. Could you implement it without using extra memory?

[leetcode]()

### Answer 
Use XOR trick. XOR has property

x1 | x2 | XOR
---|---|---
0  |0  | 0
0  |1  | 1
1  |0  | 1
1  |1  | 0

x1^x2 = x2^x1
x1^x2^x3 = x1^(x2^x3)
x1^x1 = 0
0^x1 = x1

	class Solution {
	public:
	    int singleNumber(vector<int>& nums) {
	        int result = nums[0];
	        for (int i = 1; i < nums.size(); ++i)
	        {
	            result ^= nums[i];
	        }
	        return result;
	    }
	}; 