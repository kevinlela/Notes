### Split Array with Equal Sum
Given an array with n integers, you need to find if there are triplets (i, j, k) which satisfies following conditions:

0 < i, i + 1 < j, j + 1 < k < n - 1
Sum of subarrays (0, i - 1), (i + 1, j - 1), (j + 1, k - 1) and (k + 1, n - 1) should be equal.
where we define that subarray (L, R) represents a slice of the original array starting from the element indexed L to the element indexed R.
Example:
Input: [1,2,1,2,1,2,1]
Output: True
Explanation:
i = 1, j = 3, k = 5. 
sum(0, i - 1) = sum(0, 0) = 1
sum(i + 1, j - 1) = sum(2, 2) = 1
sum(j + 1, k - 1) = sum(4, 4) = 1
sum(k + 1, n - 1) = sum(6, 6) = 1
Note:
1 <= n <= 2000.
Elements in the given array will be in range [-1,000,000, 1,000,000].

[leetcode](https://leetcode.com/problems/split-array-with-equal-sum/description/)

### Answer
One trick to skip zero, since adding zero does not change the result. 

	class Solution {
	public:
	    bool splitArray(vector<int>& nums) {
	        int len = nums.size();
	        if (len < 7) return false;
	        int stSum = 0;
	        for (int i = 0; i < len - 5; ++i)
	        {
	            stSum += nums[i];
	            if (nums[i] == 0) continue;
	            if (dfs(nums, stSum, 1, i+1)) return true;
	        }
	        
	        return false;
	    }
	    
	    bool dfs(vector<int> &nums, int stSum, int count, int idx)
	    {
	        int len = nums.size();
	        if (count == 4)
	        {
	            if (idx == len) return true;
	            else return false;
	        }
	        ++idx;
	        
	        int sum = 0;
	        bool result = false;
	        for (int i = idx; i < len - (6 - 2*count); ++i)
	        {
	            sum += nums[i];
	            if (sum == stSum)
	            {
	                if (dfs(nums, stSum, count + 1, i+1)) return true;
	            }
	        }
	        
	        return false;
	    }
	};