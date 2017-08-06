### Jump Game
Given an array of non-negative integers, you are initially positioned at the first index of the array.

Each element in the array represents your maximum jump length at that position.

Determine if you are able to reach the last index.

For example:
A = [2,3,1,1,4], return true.

A = [3,2,1,0,4], return false.

[leetcode](https://leetcode.com/problems/jump-game/description/)

### Answer 
same as [Jump Game II](45_Jump_Game_II.md)

	class Solution {
	public:
	    bool canJump(vector<int>& nums) {
	        int st = 0, ed = 0, len = nums.size();
	        
	        while (ed < len - 1)
	        {
	            int next_ed = ed;
	            for (int i = st; i <= ed; ++i)
	            {
	                next_ed = max(next_ed, i + nums[i]);
	            }
	            if (next_ed <= ed) return false; // it is not advanced
	            st = ed + 1;
	            ed = next_ed;
	        }
	        return true;
	    }
	};