### Maximum Subarray
Find the contiguous subarray within an array (containing at least one number) which has the largest sum.

For example, given the array [-2,1,-3,4,-1,2,1,-5,4],
the contiguous subarray [4,-1,2,1] has the largest sum = 6.

[leetcode](https://leetcode.com/problems/maximum-subarray/description/)

### Answer 
for a new element, the sum to include this new element is sum[i-1] + a[i]. So we need to keep sum[i-1] positive, otherwise, the new sum must be lower than a[i]. when sum[i-1] < 0, sum[i] = a[i]

	class Solution {
	public:
	    int maxSubArray(vector<int>& nums) {
	        if (nums.size() == 0) return 0;
	        int sum = nums[0], result = sum;
	        
	        for (int i = 1; i < nums.size(); ++i)
	        {
	            if (sum < 0) sum = nums[i];
	            else sum += nums[i];
	            result = max(result, sum);
	        }
	        
	        return result;
	    }
	};
