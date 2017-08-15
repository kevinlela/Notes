### Largest Divisible Subset
Given a set of distinct positive integers, find the largest subset such that every pair (Si, Sj) of elements in this subset satisfies: Si % Sj = 0 or Sj % Si = 0.

If there are multiple solutions, return any subset is fine.

Example 1:

nums: [1,2,3]

Result: \[1,2\] (of course, [1,3] will also be ok)
Example 2:

nums: [1,2,4,8]

Result: [1,2,4,8]

[leetcode](https://leetcode.com/problems/largest-divisible-subset/description/)

### Answer
If a < b and b is c's divisor so a must be c's divisor
	class Solution {
	public:
	    vector<int> largestDivisibleSubset(vector<int>& nums) {
	        int len = nums.size();
	        if (len == 0) return nums;
	        vector<int> dp(len, 0);
	        vector<int> idx(len, 0);
	        sort(nums.begin(), nums.end());
	        int maxSetIdx = 0, maxSet = 0;
	        for (int i = 0; i < len; ++i)
	        {
	            idx[i] = i;
	            dp[i] = 1;
	            for (int j = 0; j < i; ++j)
	            {
	                if (nums[i] % nums[j] == 0)
	                {
	                    //cout << nums[i] << " " << nums[j] << endl;
	                    if (dp[j] + 1 > dp[i])
	                    {
	                        idx[i] = j;
	                        dp[i] = dp[j] + 1;
	                    }
	                }
	            }
	            
	            if (dp[i] > maxSet)
	            {
	                maxSet = dp[i];
	                maxSetIdx = i;
	            }
	        }
	        
	        vector<int> result;
	        while (1)
	        {
	            result.push_back(nums[maxSetIdx]);
	            int nextIdx = idx[maxSetIdx];
	            if (nextIdx == maxSetIdx) break;
	            maxSetIdx = nextIdx;
	        }
	        
	        reverse(result.begin(), result.end());
	        return result;
	    }
	};

