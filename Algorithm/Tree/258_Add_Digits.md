### Add Digits
Given a non-negative integer num, repeatedly add all its digits until the result has only one digit.

For example:

Given num = 38, the process is like: 3 + 8 = 11, 1 + 1 = 2. Since 2 has only one digit, return it.

Follow up:
Could you do it without any loop/recursion in O(1) runtime?

[leetcode](https://leetcode.com/problems/add-digits/description/)

### Answer 
	1 - 9 
	10 - 18
	19 - 27
	This is a function with period 9

		class Solution {
		public:
		    int addDigits(int num) {
		        if (num == 0) return 0;
		        int res = num % 9;
		        return res == 0 ? 9 : res;
		    }
		};