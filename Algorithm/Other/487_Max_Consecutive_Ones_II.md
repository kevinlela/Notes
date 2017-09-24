### Max Consecutive Ones II
Given a binary array, find the maximum number of consecutive 1s in this array if you can flip at most one 0.

Example 1:
Input: [1,0,1,1,0]
Output: 4
Explanation: Flip the first zero will get the the maximum number of consecutive 1s.
    After flipping, the maximum number of consecutive 1s is 4.
Note:

The input array will only contain 0 and 1.
The length of input array is a positive integer and will not exceed 10,000
Follow up:
What if the input numbers come in one by one as an infinite stream? In other words, you can't store all numbers coming from the stream as it's too large to hold in memory. Could you solve it efficiently?

[leetcode](https://leetcode.com/problems/max-consecutive-ones-ii/description/)

### Answer
to prevent cases like [1, 0], we need to add result = max(result, count1prev + 1); to guarantee, when meet 0 at least the prev len can extend 1.

	class Solution {
	public:
	    int findMaxConsecutiveOnes(vector<int>& nums) {
	        if (nums.size() == 0) return 0;
	        int prev = 0, result = 0, count0 = 0, count1prev = 0, count1curr = 0, prevDigit = 0;
	        for (int i = 0; i < nums.size(); ++i)
	        {
	            if (nums[i] == 0) 
	            {
	                if (prevDigit = 1) 
	                {
	                    count0 = 0;
	                    count1prev = count1curr;
	                    count1curr = 0;
	                    result = max(result, count1prev + 1);
	                }
	                ++count0;
	            }
	            else 
	            {
	                ++count1curr;
	                if (count0 == 1) result = max(result, count1prev + 1 + count1curr);
	                else result = max(result, count1curr);
	            }
	            prevDigit = nums[i];
	        }
	        
	        return max(result, 1);
	    }
	};