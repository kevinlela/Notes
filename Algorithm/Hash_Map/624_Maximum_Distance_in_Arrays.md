### Maximum Distance in Arrays
Given m arrays, and each array is sorted in ascending order. Now you can pick up two integers from two different arrays (each array picks one) and calculate the distance. We define the distance between two integers a and b to be their absolute difference |a-b|. Your task is to find the maximum distance.

Example 1:
Input: 
[[1,2,3],
 [4,5],
 [1,2,3]]
Output: 4
Explanation: 
One way to reach the maximum distance 4 is to pick 1 in the first or third array and pick 5 in the second array.
Note:
Each given array will have at least 1 number. There will be at least two non-empty arrays.
The total number of the integers in all the m arrays will be in the range of [2, 10000].
The integers in the m arrays will be in the range of [-10000, 10000].

[leetcode](https://leetcode.com/problems/maximum-distance-in-arrays/description/)

### Answer
	class Solution {
	public:
	    int maxDistance(vector<vector<int>>& arrays) {
	        int result = 0;
	        map<int, int> count;
	        for (int i = 0; i < arrays.size(); ++i)
	        {
	            ++count[*arrays[i].begin()];
	            ++count[*arrays[i].rbegin()];
	        }
	        
	        for (int i = 0; i < arrays.size(); ++i)
	        {
	            int st = *arrays[i].begin();
	            int ed = *arrays[i].rbegin();
	            if (count.begin()->first != st || count.begin()->second > 1)
	                result = max(result, abs(ed - count.begin()->first));
	            if (count.rbegin()->first != ed || count.rbegin()->second > 1)
	                result = max(result, abs(st - count.rbegin()->first));
	        }
	        
	        return result;
	    }
	};