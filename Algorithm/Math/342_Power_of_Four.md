### Power of Four
Given an integer (signed 32 bits), write a function to check whether it is a power of 4.

Example:
Given num = 16, return true. Given num = 5, return false.

Follow up: Could you solve it without loops/recursion?

[leetcode](https://leetcode.com/problems/power-of-four/description/)

### Answer 
2, 4, 8, 16, 32, 64...

we can see the power of 4 only has last digit as 4 and 6

	class Solution {
	public:
	    bool isPowerOfFour(int num) {
	        int pos = 1073741824;
	        // 4^n only ends with 6 and 4
	        if (num <= 0) return false;
	        if (num == 1) return true;
	        return pos % num == 0 && (num % 10 == 6 || num % 10 == 4);
	    }
	};