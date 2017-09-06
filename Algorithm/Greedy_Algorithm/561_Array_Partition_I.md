### Array Partition I
Given an array of 2n integers, your task is to group these integers into n pairs of integer, say (a1, b1), (a2, b2), ..., (an, bn) which makes sum of min(ai, bi) for all i from 1 to n as large as possible.

Example 1:
Input: [1,4,3,2]

Output: 4
Explanation: n is 2, and the maximum sum of pairs is 4 = min(1, 2) + min(3, 4).
Note:
n is a positive integer, which is in the range of [1, 10000].
All the integers in the array will be in the range of [-10000, 10000].

[leetcode](https://leetcode.com/problems/array-partition-i/description/)

### Answer
for every element we want to add to the sum, we need sacrifice a larger element. So it is a greedy algorithm to always choose elements from large to small one the other. 

	class Solution {
	public:
	    int arrayPairSum(vector<int>& nums) {
	        // for every number you want to choose, you need a larger number to sacrifice
	        // so for x(i), we sacrifice x(i+1) because we will not sacrifice x(i+1) for x(i-1)
	        sort(nums.begin(), nums.end());
	        int result = 0;
	        for (int i = 0; i < nums.size(); i += 2)
	        {
	            result += nums[i];
	        }
	        
	        return result;
	    }
	};
