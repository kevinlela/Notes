### Reverse Bits
Reverse bits of a given 32 bits unsigned integer.

For example, given input 43261596 (represented in binary as 00000010100101000001111010011100), return 964176192 (represented in binary as 00111001011110000010100101000000).

Follow up:
If this function is called many times, how would you optimize it?

[leetcode](https://leetcode.com/problems/reverse-bits/description/)

### Answer 

	class Solution {
	public:
	    uint32_t reverseBits(uint32_t n) {
	        uint32_t mask = 0x0001;
	        uint32_t result;
	        
	        for (int i = 0; i < 32; ++i)
	        {
	            result <<= 1;
	            if (mask & n) result += 1;
	            n >>= 1;
	        }
	        
	        return result;
	    }
	};