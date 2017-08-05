### Search for a Range

Given an array of integers sorted in ascending order, find the starting and ending position of a given target value.

Your algorithm's runtime complexity must be in the order of O(log n).

If the target is not found in the array, return [-1, -1].

For example,
Given [5, 7, 7, 8, 8, 10] and target value 8,
return [3, 4].

[leetcode](https://leetcode.com/problems/search-for-a-range/description/)

###Answer

use binary search to search to boundary

	class Solution {
	public:
	    vector<int> searchRange(vector<int>& nums, int target) {
	        vector<int> result = {-1, -1};
	        if (nums.empty()) return result;
	        
	        // find the left part
	        int st = 0, ed = nums.size();
	        while (st < ed)
	        {
	            int mid = st + (ed - st)/2;
	            if (nums[mid] == target)
	            {
	                if (mid == 0 || nums[mid - 1] != target) 
	                {
	                    result[0] = mid;
	                    break;
	                }
	                else ed = mid;
	            }
	            else if (nums[mid] > target) ed = mid; //ed always larger or equal to target
	            else st = mid + 1;
	        }
	        
	        if (result[0] == -1) return result;
	        
	        st = result[0]; ed = nums.size();
	        while (st < ed)
	        {
	            int mid = st + (ed - st)/2;
	            if (nums[mid] == target)
	            {
	                if (mid == nums.size() - 1 || nums[mid + 1] != target) 
	                {
	                    result[1] = mid;
	                    break;
	                }
	                else st = mid + 1;
	            }
	            else if (nums[mid] > target) ed = mid; //ed always larger or equal to target
	            else st = mid + 1;
	        }
	        return result;
	    }
	};