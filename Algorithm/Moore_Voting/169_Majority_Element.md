### Majority Element
Given an array of size n, find the majority element. The majority element is the element that appears more than ⌊ n/2 ⌋ times.

You may assume that the array is non-empty and the majority element always exist in the array.

[leetcode](https://leetcode.com/problems/majority-element/description/)

### Answer 
find element in [n/k] times. 
1) construct vector of k elements
2) if n[i] == v[k]; v[k]++;
3) else all ==v[k]
4) if v[k] == 0 assign n[i] to v[k]
5) count v[k] again. 

	class Solution {
	public:
	    int majorityElement(vector<int>& nums) {
	        if (nums.size() == 0) return -1;
	        int maj = nums[0], majCount = 1;
	        
	        for (int k = 1; k < nums.size(); ++k)
	        {
	            if (maj == nums[k]) ++majCount;
	            else if (majCount == 0)
	            {
	                ++majCount;
	                maj = nums[k];
	            }
	            else --majCount;
	        }
	        
	        return maj;
	    }
	};