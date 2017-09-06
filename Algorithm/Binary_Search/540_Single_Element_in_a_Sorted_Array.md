### Single Element in a Sorted Array
Given a sorted array consisting of only integers where every element appears twice except for one element which appears once. Find this single element that appears only once.

Example 1:
Input: [1,1,2,3,3,4,4,8,8]
Output: 2
Example 2:
Input: [3,3,7,7,10,11,11]
Output: 10

[leetcode](https://leetcode.com/problems/single-element-in-a-sorted-array/description/)

### Answer
It is natural to think about binary search when meet a problem like find sth in a sorted array. 

every mid point check left and right to see whether there is one same as current one. 

	class Solution {
	public:
	    int singleNonDuplicate(vector<int>& nums) {
	        //the length must be odd
	        
	        int len = nums.size(), st = 0, ed = len;
	        while (st < ed)
	        {
	            int mid = st + (ed - st)/2;
	            if (mid - 1 >= 0 && nums[mid-1] == nums[mid])
	            {
	                int len2end = ed - mid - 1;
	                if (len2end % 2 != 0) st = mid + 1;
	                else ed = mid - 1;
	            }
	            else if (mid + 1 < len && nums[mid+1] == nums[mid])
	            {
	                int len2end = ed - mid - 2;
	                if (len2end % 2 != 0) st = mid + 2;
	                else ed = mid;
	            }
	            else return nums[mid];
	        }
	        
	        return -1;
	    }
	};