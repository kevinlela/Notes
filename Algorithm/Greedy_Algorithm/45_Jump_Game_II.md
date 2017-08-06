### Jump Game II

Given an array of non-negative integers, you are initially positioned at the first index of the array.

Each element in the array represents your maximum jump length at that position.

Your goal is to reach the last index in the minimum number of jumps.

For example:
Given array A = [2,3,1,1,4]

The minimum number of jumps to reach the last index is 2. (Jump 1 step from index 0 to 1, then 3 steps to the last index.)

Note:
You can assume that you can always reach the last index.

[leetcode](https://leetcode.com/problems/jump-game-ii/description/)

### Answer 
For every search interval, we just need to find the next end point

	class Solution {
	public:
	    int jump(vector<int>& nums) {
	        if (nums.size() <= 1) return 0;
	        
	        int step = 0, st= 0, curr = 0;
	        while (curr < nums.size() - 1)
	        {
	            int next = 0;
	            for (int i = st; i <= curr && nums.size(); ++i)
	            {
	                next = max(next, nums[i] + i);
	            }
	            st = curr + 1;
	            curr = next;
	            step++;
	        }
	        
	        return step;
	    }
	};