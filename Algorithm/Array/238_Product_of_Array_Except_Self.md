### Product of Array Except Self
Given an array of n integers where n > 1, nums, return an array output such that output[i] is equal to the product of all the elements of nums except nums[i].

Solve it without division and in O(n).

For example, given [1,2,3,4], return [24,12,8,6].

Follow up:
Could you solve it with constant space complexity? (Note: The output array does not count as extra space for the purpose of space complexity analysis.)

[leetcode](https://leetcode.com/problems/product-of-array-except-self/description/)

### Answer
let L[i] be the product of all element left to i and R[i] to be the product of all elements right to i. the result P[i] = L[i] * R[i]

	class Solution {
	public:
	    vector<int> productExceptSelf(vector<int>& nums) {
	        int len = nums.size();
	        if (len == 0) return vector<int>();
	        if (len == 1) return vector<int>(1, 0);
	        
	        vector<int> result(len, 1);
	        int prev = 1;
	        
	        for (int i = 0; i < len; ++i)
	        {
	            result[i] = prev;
	            prev *= nums[i];
	        }
	        
	        prev = 1;
	        
	        for (int i = len - 1; i >= 0; --i)
	        {
	            result[i] *= prev;
	            prev *= nums[i];
	        }
	        
	        return result;
	    }
	};