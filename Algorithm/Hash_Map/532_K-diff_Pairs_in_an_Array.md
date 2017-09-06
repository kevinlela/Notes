### K-diff Pairs in an Array
Given an array of integers and an integer k, you need to find the number of unique k-diff pairs in the array. Here a k-diff pair is defined as an integer pair (i, j), where i and j are both numbers in the array and their absolute difference is k.

Example 1:
Input: [3, 1, 4, 1, 5], k = 2
Output: 2
Explanation: There are two 2-diff pairs in the array, (1, 3) and (3, 5).
Although we have two 1s in the input, we should only return the number of unique pairs.
Example 2:
Input:[1, 2, 3, 4, 5], k = 1
Output: 4
Explanation: There are four 1-diff pairs in the array, (1, 2), (2, 3), (3, 4) and (4, 5).
Example 3:
Input: [1, 3, 1, 5, 4], k = 0
Output: 1
Explanation: There is one 0-diff pair in the array, (1, 1).
Note:
The pairs (i, j) and (j, i) count as the same pair.
The length of the array won't exceed 10,000.
All the integers in the given input belong to the range: [-1e7, 1e7].

[leetcode](https://leetcode.com/problems/k-diff-pairs-in-an-array/description/)

### Answer
It is a hash problem. |nums[j] - nums[i]| = k. 

nums[j] = k + nums[i]
nums[j] = nums[i] - k

So we just need to store the k + nums[i] and nums[i] - k. 

	class Solution {
	public:
	    int findPairs(vector<int>& nums, int k) {
	        if (k < 0) return 0;
	        unordered_map<int, int> counts;
	        for (int i = 0; i < nums.size(); ++i)
	        {
	            counts[nums[i]]++;
	        }
	        
	        int result = 0;
	        for (auto iter = counts.begin(); iter != counts.end(); ++iter)
	        {
	            int target = iter->first + k;
	            if (counts.find(target) == counts.end()) continue;
	            else if (target == iter->first)
	            {
	                if(iter->second > 1) ++result;
	            }
	            else ++result;
	        }
	            
	        return result;
	    }
	};


