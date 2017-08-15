### Wiggle Subsequence *
A sequence of numbers is called a wiggle sequence if the differences between successive numbers strictly alternate between positive and negative. The first difference (if one exists) may be either positive or negative. A sequence with fewer than two elements is trivially a wiggle sequence.

For example, [1,7,4,9,2,5] is a wiggle sequence because the differences (6,-3,5,-7,3) are alternately positive and negative. In contrast, [1,4,7,2,5] and [1,7,4,5,5] are not wiggle sequences, the first because its first two differences are positive and the second because its last difference is zero.

Given a sequence of integers, return the length of the longest subsequence that is a wiggle sequence. A subsequence is obtained by deleting some number of elements (eventually, also zero) from the original sequence, leaving the remaining elements in their original order.

Examples:
Input: [1,7,4,9,2,5]
Output: 6
The entire sequence is a wiggle sequence.

Input: [1,17,5,10,13,15,10,5,16,8]
Output: 7
There are several subsequences that achieve this length. One is [1,17,10,13,10,16,8].

Input: [1,2,3,4,5,6,7,8,9]
Output: 2
Follow up:
Can you do it in O(n) time?

[leetcode](https://leetcode.com/problems/wiggle-subsequence/description/)

### Answer
I made quite messy solution this time so I copy the solution the first time. Since we maitian two status odd and even to indicate when the coming one is odd or even. Here is a greedy sense that if the comming one is not odd, it can lower the even and vice versa. 

	class Solution {
	public:
	    int wiggleMaxLength(vector<int>& nums) {
	        //for every element i, we check if it can get even or odd
	        //if even, we need num[i] < num[j], j < i
	        //if num[i] < num[i-1], we just need to len + 1;
	        //if not, because num[i-2] < num[i-1], num[i] can replace num[i-2]
	        int len = nums.size();
	        if (len <= 1) return len;
	        vector<int> even(len, 0);
	        vector<int> odd(len, 0);
	        
	        even[0] = 1; 
	        odd[0] = 1;
	        
	        for (int k = 1; k < len; k++)
	        {
	            //if want to be even
	            if (nums[k] < nums[k-1]) even[k] = odd[k-1] + 1;
	            else even[k] = even[k-1];
	            
	            //if want to be odd
	            if (nums[k] > nums[k-1]) odd[k] = even[k-1] + 1;
	            else odd[k] = odd[k-1];
	        }
	        return max(odd[len-1], even[len-1]);
	        
	    }
	};


