### Search in Rotated Sorted Array

Suppose an array sorted in ascending order is rotated at some pivot unknown to you beforehand.

(i.e., 0 1 2 4 5 6 7 might become 4 5 6 7 0 1 2).

You are given a target value to search. If found in the array return its index, otherwise return -1.

You may assume no duplicate exists in the array.

[leetcode](https://leetcode.com/problems/search-in-rotated-sorted-array/description/)

### Answer

for all kinds of binary search problem, we need to answer the binary decision question first. For this problem, e.g., we need to figure out which half is in normal order and can help use make the decision. 

	class Solution {
	public:
	    int search(vector<int>& nums, int target) {
	        // mid < end -> right part is OK
	        // mid > end -> left part is OK
	        
	        if (nums.size() == 0) return -1;
	        
	        int st = 0, ed = nums.size() - 1;
	        while (st <= ed)
	        {
	            int mid = st + (ed - st) / 2;
	            if (nums[mid] == target) return mid;
	            if (nums[mid] < nums[ed]) // right part is OK
	            {
	                if (nums[ed] == target) return ed;
	                if (nums[mid] < target && nums[ed] > target) st = mid + 1;
	                else ed = mid - 1;
	            }
	            else // left part is OK
	            {
	                if (nums[st] == target) return st;
	                if (nums[mid] > target && nums[st] < target) ed = mid - 1;
	                else st = mid + 1;
	            }
	        }
	        
	        return -1;
	        
	    }
	};