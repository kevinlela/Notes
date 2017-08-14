### Number of 1 Bits
Write a function that takes an unsigned integer and returns the number of ’1' bits it has (also known as the Hamming weight).

For example, the 32-bit integer ’11' has binary representation 00000000000000000000000000001011, so the function should return 3.

[leetcode](https://leetcode.com/problems/number-of-1-bits/description/)

### Answer 

	class Solution {
	public:
	    int hammingWeight(uint32_t n) {
	        uint32_t mask = 0x0001;
	        int result = 0;
	        while (n)
	        {
	            if (mask & n) ++result;
	            n >>= 1;
	        }
	        return result;
	    }
	};