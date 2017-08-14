### Minimum Size Subarray Sum
Given an array of n positive integers and a positive integer s, find the minimal length of a contiguous subarray of which the sum ≥ s. If there isn't one, return 0 instead.

For example, given the array [2,3,1,2,4,3] and s = 7,
the subarray [4,3] has the minimal length under the problem constraint.

click to show more practice.

More practice:
If you have figured out the O(n) solution, try coding another solution of which the time complexity is O(n log n).

[leetcode](https://leetcode.com/problems/minimum-size-subarray-sum/description/)

### Answer 
Once the sum in the window larger than s, shrink the window to make it invalid. 

	class Solution {
	public:
	    int minSubArrayLen(int s, vector<int>& nums) {
	        int len = nums.size();
	        int st = 0, ed = 0;
	        int sum = 0, res = INT_MAX;
	        
	        for (int k = 0; k < len; ++k)
	        {
	            sum += nums[k];
	            
	            while (st <= k && sum >= s)
	            {
	                res = min(res, k - st + 1);
	                sum -= nums[st++];
	            }
	            if (res == 1) return res;
	        }
	        
	        return res == INT_MAX ? 0 : res;
	    }
	};