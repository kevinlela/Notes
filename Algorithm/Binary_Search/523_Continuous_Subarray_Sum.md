### Continuous Subarray Sum
Given a list of non-negative numbers and a target integer k, write a function to check if the array has a continuous subarray of size at least 2 that sums up to the multiple of k, that is, sums up to n*k where n is also an integer.

Example 1:
Input: [23, 2, 4, 6, 7],  k=6
Output: True
Explanation: Because [2, 4] is a continuous subarray of size 2 and sums up to 6.
Example 2:
Input: [23, 2, 6, 4, 7],  k=6
Output: True
Explanation: Because [23, 2, 6, 4, 7] is an continuous subarray of size 5 and sums up to 42.
Note:
The length of the array won't exceed 10,000.
You may assume the sum of all the numbers is in the range of a signed 32-bit integer.

[leetcode](https://leetcode.com/problems/continuous-subarray-sum/description/)

### Answer

We need to balance, if we use brutal force, O(N)
use binary search, we achieve O(NlogN * T/k), T is all possible sum 

	class Solution {
	public:
	    bool checkSubarraySum(vector<int>& nums, int k) {
	        if (k < 0) k = -k;
	        if (nums.size() < 2) return false;
	        
	        vector<int> sums(1, 0);
	        int prev = 0;
	        for (int i = 0; i < nums.size(); ++i)
	        {
	            prev += nums[i];
	            sums.push_back(prev);
	        }
	        
	        if (k == 1 && *sums.rbegin() != 0) return true;
	        for (auto iter = sums.begin() + 2; iter != sums.end(); ++iter)
	        {
	            auto st = sums.begin(), ed = iter;
	            // sum[i] - sum[j] = n*k
	            for (int t = 0; t <= *iter; t += k)
	            {
	                auto it = lower_bound(st, ed, *iter - t);
	                if (it != sums.end() && *it == *iter - t && iter - it >= 2) return true;
	                if (k == 0) break;
	            }
	        }
	        
	        return false;
	    }
	};