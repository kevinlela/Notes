### Contiguous Array
Given a binary array, find the maximum length of a contiguous subarray with equal number of 0 and 1.

Example 1:
Input: [0,1]
Output: 2
Explanation: [0, 1] is the longest contiguous subarray with equal number of 0 and 1.
Example 2:
Input: [0,1,0]
Output: 2
Explanation: [0, 1] (or [1, 0]) is a longest contiguous subarray with equal number of 0 and 1.
Note: The length of the given binary array will not exceed 50,000.


[leetcode](https://leetcode.com/problems/contiguous-array/description/)

### Answer
The window of equal number of 0 and 1 means, with len = 2*sum

len = 2*(sum[j] - sum[i])
j - i = 2*sum[j] - 2*sum[i]

2*sum[i] - i = 2*sum[j] - j

That is a hash map problem, the value is 2*sum[i] - i

	class Solution {
	public:
	    int findMaxLength(vector<int>& nums) {
	        // if we have a window with equal 1 and zero
	        // now we meet an zero, is there any possibility we include this zero without modify the win?
	        // what about +2 zero? 
	        // no, it seems two pointers do not work
	        // can we know the number of 1 in an interval?
	        // use sum but still O(N^2)
	        // give up
	        // see the answer
	        // the number of 1 can be expressed as sum[j] - sum[i] the sum between (i, j)
	        // we want to find sum[j] - sum[i] = (j-i)/2
	        // 2sump[j] - j = 2sum[i] - i
	        
	        unordered_map<int, int> um;
	        int sum = 0, result = 0, i = 0;
	        um[0] = 0;
	        
	        for (i; i < nums.size(); ++i)
	        {
	            sum += nums[i];
	            int target = 2*sum - i - 1;
	            if (um.find(target) == um.end()) um[target] = i + 1;
	            else result = max(result, i + 1 - um[target]);
	        }
	        return result;
	    }
	};