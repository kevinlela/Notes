### Find Minimum in Rotated Sorted Array II
Follow up for "Find Minimum in Rotated Sorted Array":
What if duplicates are allowed?

Would this affect the run-time complexity? How and why?
Suppose an array sorted in ascending order is rotated at some pivot unknown to you beforehand.

(i.e., 0 1 2 4 5 6 7 might become 4 5 6 7 0 1 2).

Find the minimum element.

The array may contain duplicates.

[leetcode](https://leetcode.com/problems/find-minimum-in-rotated-sorted-array-ii/description/)

### Answer 
same as [81](81_Search_in_Rotated_Sorted_Array_II.md)

	class Solution {
	public:
	    int findMin(vector<int>& nums) {
	        int len = nums.size();
	        if (len == 0) return -1;
	        int st = 0, ed = len - 1;
	        
	        while (st < ed)
	        {
	            int mid = st + (ed - st)/2;
	            if (nums[mid] < nums[ed]) // the right side is OK
	            {
	                ed = mid;
	            }
	            else if (nums[mid] > nums[ed]) 
	            {
	                st = mid + 1;
	            }
	            else --ed;
	        }
	        
	        return nums[ed];
	    }
	};