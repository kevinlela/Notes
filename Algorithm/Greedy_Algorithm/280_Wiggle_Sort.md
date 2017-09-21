### Wiggle Sort
Given an unsorted array nums, reorder it in-place such that nums[0] <= nums[1] >= nums[2] <= nums[3]....

For example, given nums = [3, 5, 2, 1, 6, 4], one possible answer is [1, 6, 2, 5, 3, 4].

[leetcode](https://leetcode.com/problems/wiggle-sort/description/)

### Answer

	class Solution {
	public:
	    void wiggleSort(vector<int>& nums) {
	        // n[0], n[1]
	        // two cases :
	        // n[2] > n[1], since n[1] > n[0], swap n[2] and n[1] has no problem
	        // n[1] >= n[2], just keep it
	        // conversely for even entry
	        
	        if (nums.size() <= 1) return;
	        if (nums[0] >nums[1]) swap(nums[0], nums[1]);
	        
	        for (int i = 2; i < nums.size(); ++i)
	        {
	            if (i % 2)
	            {
	                if (nums[i] < nums[i-1]) swap(nums[i], nums[i-1]);
	            }
	            else
	            {
	                if (nums[i] > nums[i-1]) swap(nums[i], nums[i-1]);
	            }
	        }
	    }
	};