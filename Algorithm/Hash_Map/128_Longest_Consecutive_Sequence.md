### Longest Consecutive Sequence
Given an unsorted array of integers, find the length of the longest consecutive elements sequence.

For example,
Given [100, 4, 200, 1, 3, 2],
The longest consecutive elements sequence is [1, 2, 3, 4]. Return its length: 4.

Your algorithm should run in O(n) complexity.

[leetcode](https://leetcode.com/problems/longest-consecutive-sequence/description/)

### Answer 
Create a hashmap and find the sequence. 

	class Solution {
	public:
	    int longestConsecutive(vector<int>& nums) {
	        unordered_set<int> allNums(nums.begin(), nums.end());
	        
	        int maxLen = 0;
	        while (!allNums.empty())
	        {
	            int curr = *(allNums.begin());
	            allNums.erase(curr);
	            int len = 1;
	            int right = curr + 1;
	            while (allNums.find(right) != allNums.end())
	            {
	                allNums.erase(right);
	                ++len;
	                ++right;
	            }
	            
	            int left = curr - 1;
	            while (allNums.find(left) != allNums.end())
	            {
	                allNums.erase(left);
	                ++len;
	                --left;
	            }
	            maxLen = max(maxLen, len);
	        }
	        
	        return maxLen;
	    }
	};