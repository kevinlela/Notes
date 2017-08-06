### Remove Duplicates from Sorted Array II
Follow up for "Remove Duplicates":
What if duplicates are allowed at most twice?

For example,
Given sorted array nums = [1,1,1,2,2,3],

Your function should return length = 5, with the first five elements of nums being 1, 1, 2, 2 and 3. It doesn't matter what you leave beyond the new length.

[leetcode](https://leetcode.com/problems/remove-duplicates-from-sorted-array-ii/description/)

### Answer 
Use two pointer but need a variable to record the occurence of current value

	class Solution {
	public:
	    int removeDuplicates(vector<int>& nums) {
	        if (nums.size() == 0) return 0;
	        int count = 1, curr = 1, currVal = nums[0];
	        for (int i = 1; i < nums.size(); ++i)
	        {
	            if (nums[i] == currVal && count == 1)
	            {
	                ++count;
	                swap(nums[curr++], nums[i]);
	            }
	            else if (nums[i] != currVal)
	            {
	                count = 1;
	                currVal = nums[i];
	                swap(nums[curr++], nums[i]);
	            }
	        }
	        
	        return curr;
	    }
	};