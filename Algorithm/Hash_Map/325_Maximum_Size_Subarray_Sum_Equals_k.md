### Maximum Size Subarray Sum Equals k
Given an array nums and a target value k, find the maximum length of a subarray that sums to k. If there isn't one, return 0 instead.

Note:
The sum of the entire nums array is guaranteed to fit within the 32-bit signed integer range.

Example 1:
Given nums = [1, -1, 5, -2, 3], k = 3,
return 4. (because the subarray [1, -1, 5, -2] sums to 3 and is the longest)

Example 2:
Given nums = [-2, -1, 2, 1], k = 1,
return 2. (because the subarray [-1, 2] sums to 1 and is the longest)

Follow Up:
Can you do it in O(n) time?

[leetcode](https://leetcode.com/problems/maximum-size-subarray-sum-equals-k/description/)

### Answer

	class Solution {
	public:
	    int maxSubArrayLen(vector<int>& nums, int k) {
	        unordered_map<int, int> sum;
	        sum[0] = -1;
	        
	        int all_sum = 0;
	        int result = 0;
	        for (int i = 0; i < nums.size(); ++i)
	        {
	            all_sum += nums[i];
	            // find all_sum - sum = k -> sum = all_sum - k
	            if (sum.find(all_sum - k) != sum.end()) result = max(result, i - sum[all_sum - k]);
	            if (sum.find(all_sum) == sum.end()) sum[all_sum] = i;
	        }
	        
	        return result;
	    }
	};