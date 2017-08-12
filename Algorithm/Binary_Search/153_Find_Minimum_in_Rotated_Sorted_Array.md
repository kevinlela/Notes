### Find Minimum in Rotated Sorted Array
Suppose an array sorted in ascending order is rotated at some pivot unknown to you beforehand.

(i.e., 0 1 2 4 5 6 7 might become 4 5 6 7 0 1 2).

Find the minimum element.

You may assume no duplicate exists in the array.

[leetcode](https://leetcode.com/problems/find-minimum-in-rotated-sorted-array/description/)

### Answer 
it is same as [33](33_Search_in_Rotated_Sorted_Array.md)

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
	            else 
	            {
	                st = mid + 1;
	            }
	        }
	        
	        return nums[ed];
	    }
	};