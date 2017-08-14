### Power of Three
Given an integer, write a function to determine if it is a power of three.

Follow up:
Could you do it without using any loop / recursion?

[leetcode](https://leetcode.com/problems/power-of-three/description/)

### Answer 
Same as [231](231_Power_of_Two.md)

	class Solution {
	public:
	    bool isPowerOfThree(int n) {
	        int maxThree = 1162261467;
	        if (n <= 0) return false;
	        return maxThree % n == 0;
	    }
	};