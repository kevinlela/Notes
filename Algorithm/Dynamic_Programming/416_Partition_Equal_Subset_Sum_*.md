### Partition Equal Subset Sum *
Given a non-empty array containing only positive integers, find if the array can be partitioned into two subsets such that the sum of elements in both subsets is equal.

Note:
Each of the array element will not exceed 100.
The array size will not exceed 200.
Example 1:

Input: [1, 5, 11, 5]

Output: true

Explanation: The array can be partitioned as [1, 5, 5] and [11].
Example 2:

Input: [1, 2, 3, 5]

Output: false

Explanation: The array cannot be partitioned into equal sum subsets.

[leetcode](https://leetcode.com/problems/partition-equal-subset-sum/description/)

### Answer 
we can get the total sum. if the sum is odd, then it is impossible. then the problem becomes, whether we can find elements in an array sum up to sum/2. It is a dp problem. Notice, it is not coin change problem, since only element can only be used once. this is why the loop has nums first and sum at second. 

	class Solution {
	public:
	    bool canPartition(vector<int>& nums) {
	        // the brutal force idea is using dfs
	        // the dp problem is like coin change problem
	        int sum = 0;
	        for (int i = 0; i < nums.size(); ++i)
	        {
	            sum += nums[i];
	        }
	        if (sum % 2 != 0) return false;
	        sum /= 2;
	        vector<bool> dp(sum + 1, false);
	        dp[0] = true;
	        for (int i = 0; i < nums.size(); ++i)
	        {
	            for (int j = sum; j >= nums[i]; --j)
	            {
	                dp[j] = dp[j] || dp[j-nums[i]];
	            }
	        }
	        
	        return dp[sum];
	    }
	}; 