### Contains Duplicate
Given an array of integers, find if the array contains any duplicates. Your function should return true if any value appears at least twice in the array, and it should return false if every element is distinct.


[leetcode](https://leetcode.com/problems/contains-duplicate/description/)

### Answer 

	class Solution {
	public:
	    bool containsDuplicate(vector<int>& nums) {
	        unordered_set<int> us(nums.begin(), nums.end());
	        return nums.size() != us.size();
	    }
	};