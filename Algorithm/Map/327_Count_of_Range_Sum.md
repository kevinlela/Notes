### Count of Range Sum
Given an integer array nums, return the number of range sums that lie in [lower, upper] inclusive.
Range sum S(i, j) is defined as the sum of the elements in nums between indices i and j (i ? j), inclusive.

Note:
A naive algorithm of O(n2) is trivial. You MUST do better than that.

Example:
Given nums = [-2, 5, -1], lower = -2, upper = 2,
Return 3.
The three ranges are : [0, 0], [2, 2], [0, 2] and their respective sums are: -2, -1, 2.

[leetcode](https://leetcode.com/problems/count-of-range-sum/description/)

### Answer 
we can get sum[j] represents sum(S[0]...S[j]) sum[j] - sum[i] is the interval
lower < sum[j] - sum[i] < upper

	class Solution {
	public:
	    int countRangeSum(vector<int>& nums, int lower, int upper) {
	        // lower < sum[i...j] < upper
	        // lower < sum[j] - sum[i] < upper
	        // equals to is there an i before j such that the equation above works?
	        
	        multiset<long> sums;
	        sums.insert(0);
	        long add = 0, result = 0;
	        for (int i = 0; i < nums.size(); ++i)
	        {
	            add += nums[i];
	            // sum[i] > sum[j] - upper
	            auto lb = sums.lower_bound(add - upper);
	            // sum[i] < sum[j] - lower
	            auto ub = sums.upper_bound(add - lower);
	            int dis = distance(lb, ub);
	            result += dis < 0 ? 0 : (dis );
	            sums.insert(add);
	        }
	        
	        return result;
	    }
	};