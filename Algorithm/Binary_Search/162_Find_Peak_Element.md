### Find Peak Element
A peak element is an element that is greater than its neighbors.

Given an input array where num[i] ≠ num[i+1], find a peak element and return its index.

The array may contain multiple peaks, in that case return the index to any one of the peaks is fine.

You may imagine that num[-1] = num[n] = -∞.

For example, in array [1, 2, 3, 1], 3 is a peak element and your function should return the index number 2.

click to show spoilers.

Note:
Your solution should be in logarithmic complexity.

[leetcode](https://leetcode.com/problems/find-peak-element/description/)

### Answer 
We can use three points to determine whether it is peak, up or down. 

	class Solution {
	public:
	    int findPeakElement(vector<int>& nums) {
	        int len = nums.size();
	        if (len == 0) return -1;
	        int st = 0, ed = len-1;
	        
	        while (st < ed)
	        {
	            int mid = st + (ed - st)/2;
	            int prev = mid == 0 ? INT_MIN : nums[mid - 1];
	            int next = mid == len -1 ? INT_MIN : nums[mid + 1];
	            int curr = nums[mid];
	            
	            if (prev <= curr && curr >= next ) return mid;
	            else if (prev <= curr && curr <= next) st = mid + 1;
	            else if (prev >= curr && curr >= next) ed = mid;
	            else st = mid + 1;
	        }
	        
	        return st;
	    }
	};