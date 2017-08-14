### Bitwise AND of Numbers Range
Given a range [m, n] where 0 <= m <= n <= 2147483647, return the bitwise AND of all numbers in this range, inclusive.

For example, given the range [5, 7], you should return 4.

[leetcode](https://leetcode.com/problems/bitwise-and-of-numbers-range/description/)

### Answer 

The period of switch for each bit is 2^(i-1). So we just need to detect the range. 


	class Solution {
	public:
	    int rangeBitwiseAnd(int m, int n) {
	        int mask = 1;
	        int result = m & n;
	        for (int k = 0; k < 32; ++k)
	        {
	            if (n - m > mask) result &= ~mask;
	            else break;
	            mask <<= 1;
	        }
	        
	        return result;
	    }
	};