### Contains Duplicate III
Given an array of integers, find out whether there are two distinct indices i and j in the array such that the absolute difference between nums[i] and nums[j] is at most t and the absolute difference between i and j is at most k.

[leetcode](https://leetcode.com/problems/contains-duplicate-iii/description/)

### Answer 
Use multimap to track and sort all element in a window with length k

|a[i] - a[k]| <= t
equals to  a[i] - a[k] <= t  && a[i] - a[k] >= -t

a[k] >= a[i] - t -> this is lower bound of the multimap

a[k] <= a[i] + t -> this can be checked after we find a[k] since any element right to a[k] is larger than a[k]

	class Solution {
	public:
	    bool containsNearbyAlmostDuplicate(vector<int>& nums, int k, int t) {
	        if (k == 0) return false;
	        set<long> win;
	        int st = 0;
	        
	        for (int i = 0; i < nums.size(); ++i)
	        {
	            if (win.size() > k) win.erase(nums[st++]);
	            auto iter = win.lower_bound((long)nums[i] - (long)t);
	            if (iter != win.end() 
	                && (long)*iter - (long)t <= (long)nums[i]) return true;
	            win.insert(nums[i]);
	        }
	        
	        return false;
	    }
	};