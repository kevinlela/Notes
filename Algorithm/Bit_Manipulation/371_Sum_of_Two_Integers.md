### Sum of Two Integers
Calculate the sum of two integers a and b, but you are not allowed to use the operator + and -.

Example:
Given a = 1 and b = 2, return 3.

[leetcode](https://leetcode.com/problems/sum-of-two-integers/description/)

### Answer
Calculate no carry by XOR
calculate carry by &
shift the carry to left to add to next iteration

	class Solution {
	public:
	    int getSum(int a, int b) {
	        int ans = a^b;
	        int c = a & b;
	        while (c)
	        {
	            c <<= 1;
	            int tmp = ans ^ c; // this operation gives the sum without any carry
	            c = ans & c; // this operation gives carry, since we need to add this carry to be left shift ` so we shift it at the beginning of the loop
	            ans = tmp;
	        }
	        return ans;
	    }
	};