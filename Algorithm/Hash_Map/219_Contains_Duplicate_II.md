### Contains Duplicate II
Given an array of integers and an integer k, find out whether there are two distinct indices i and j in the array such that nums[i] = nums[j] and the absolute difference between i and j is at most k.

[leetcode](https://leetcode.com/problems/contains-duplicate-ii/description/)

### Answer 
Window version of [217](217_Contains_Duplicate.md)
	class Solution {
	public:
	    bool containsNearbyDuplicate(vector<int>& nums, int k) {
	        if (k <= 0) return false;
	        unordered_set<int> win;
	        int st = 0;
	        for (int i = 0; i < nums.size(); ++i)
	        {
	            if (win.size() > k) win.erase(nums[st++]);
	            if (win.find(nums[i]) != win.end()) return true;
	            win.insert(nums[i]);
	        }
	        return false;
	    }
	};