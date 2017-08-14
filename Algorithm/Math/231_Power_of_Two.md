### Power of Two
Given an integer, write a function to determine if it is a power of two.

[leetcode](https://leetcode.com/problems/power-of-two/description/)

### Answer 
This is the trick, use 2^{max_N} as dividend. and the n as divisor. If we can devide, n must be power of 2. 

	class Solution {
	public:
	    bool isPowerOfTwo(int n) {
	        if (n <= 0) return false;
	        int max = 2147483648;
	        return max % n == 0;
	    }
	};