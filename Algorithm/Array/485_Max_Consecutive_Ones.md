### Max Consecutive Ones
Given a binary array, find the maximum number of consecutive 1s in this array.

Example 1:
Input: [1,1,0,1,1,1]
Output: 3
Explanation: The first two digits or the last three digits are consecutive 1s.
    The maximum number of consecutive 1s is 3.
Note:

The input array will only contain 0 and 1.
The length of input array is a positive integer and will not exceed 10,000

[leetcode](https://leetcode.com/problems/max-consecutive-ones/description/)

### Answer

	class Solution {
	public:
	    int findMaxConsecutiveOnes(vector<int>& nums) {
	        int c1 = 0, res = 0;
	        for (int i = 0; i < nums.size(); ++i)
	        {
	            if (nums[i] == 0) 
	            {   
	                res = max(res, c1);
	                c1 = 0;
	            }
	            else ++c1;
	        }
	        
	        return max(res, c1);
	    }
	};