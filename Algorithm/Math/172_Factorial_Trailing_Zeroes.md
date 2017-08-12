### Factorial Trailing Zeroes
Given an integer n, return the number of trailing zeroes in n!.

Note: Your solution should be in logarithmic time complexity.

[leetcode](https://leetcode.com/problems/factorial-trailing-zeroes/description/)

### Answer 
only 2 and 5 combines to tail 0, since 2 is much more than 5, so we are country how many 5. n/5 is the result. However, for the power of 5 say 25, there is an extra 5. we need to consider this situation. 

	class Solution {
	public:
	    int trailingZeroes(int n) {
	        // n! = n x (n-1) x ... x 1
	        // 0 comes from 2 and 5, since 2's number is way more than 5's
	        // we only need to count 5, how many 5 appears in n
	        // however, 25 has two 5, similarly 125 has three 5
	        // after 5, we need to count how many 25
	        long base = 5, nL = n;
	        int result = 0;
	        while (1)
	        {
	            int count = nL/base;
	            if (count == 0) break;
	            result += count;
	            base *= 5;
	        }
	        return result;
	    }
	};