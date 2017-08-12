### Two Sum II - Input array is sorted
Given an array of integers that is already sorted in ascending order, find two numbers such that they add up to a specific target number.

The function twoSum should return indices of the two numbers such that they add up to the target, where index1 must be less than index2. Please note that your returned answers (both index1 and index2) are not zero-based.

You may assume that each input would have exactly one solution and you may not use the same element twice.

Input: numbers={2, 7, 11, 15}, target=9
Output: index1=1, index2=2

[leetcode](https://leetcode.com/problems/two-sum-ii-input-array-is-sorted/description/)

### Answer 
It is the sub problem of [15](15_3Sum.md)

	class Solution {
	public:
	    vector<int> twoSum(vector<int>& numbers, int target) {
	        int len = numbers.size();
	        vector<int> result(2, 0);
	        result[0] = 0; result[1] = len - 1;
	        while (result[0] < result[1])
	        {
	            int total = numbers[result[0]] + numbers[result[1]];
	            if (total == target) 
	            {
	                result[0] += 1;
	                result[1] += 1;
	                return result;
	            }
	            else if (total > target) --result[1];
	            else ++result[0];
	        }
	        
	        return result;
	    }
	};