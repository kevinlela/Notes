### Remove Element

Given an array and a value, remove all instances of that value in place and return the new length.

Do not allocate extra space for another array, you must do this in place with constant memory.

The order of elements can be changed. It doesn't matter what you leave beyond the new length.

Example:
Given input array nums = [3,2,2,3], val = 3

Your function should return length = 2, with the first two elements of nums being 2.

[leetcode](https://leetcode.com/problems/remove-element/description/)

### Answer

use a point starting from the end and move the target value to that point end back advancing 

	class Solution {
	public:
	    int removeElement(vector<int>& nums, int val) {
	        if (nums.size() == 0) return 0;
	        int st = 0, ed = nums.size() - 1;
	        while (st <= ed)
	        {
	            if (nums[st] == val) swap(nums[st], nums[ed--]);
	            else st++;
	        }
	        return st;
	    }
	};