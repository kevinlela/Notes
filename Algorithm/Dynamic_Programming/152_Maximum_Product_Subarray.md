### Maximum Product Subarray
Find the contiguous subarray within an array (containing at least one number) which has the largest product.

For example, given the array [2,3,-2,4],
the contiguous subarray [2,3] has the largest product = 6.

[leetcode](https://leetcode.com/problems/maximum-product-subarray/description/)

### Answer 
There are two states of this problem, when one is neg * prev_neg, one is pos * prev_neg. So we maintain two dp array. 

	class Solution {
	public:
	    int maxProduct(vector<int>& nums) {
	        // there are two cases
	        // the maximum number either comes from negative or positive
	        // maintain the negative and positive number
	        // neg[i] record the smallest negative product until ith element
	        // pos[i] record the largest positive product until ith element
	        if (nums.size() == 0) return 0;
	        int posPrev = nums[0], negPrev = nums[0], result = nums[0];
	        
	        for (int k = 1; k < nums.size(); ++k)
	        {
	            int posPrevTmp = max(nums[k], max(posPrev*nums[k], negPrev*nums[k]));
	            int negPrevTmp = min(nums[k], min(posPrev*nums[k], negPrev*nums[k]));
	            posPrev = posPrevTmp;
	            negPrev = negPrevTmp;
	            result = max(result, posPrev);
	        }
	        
	        return result;
	    }
	};