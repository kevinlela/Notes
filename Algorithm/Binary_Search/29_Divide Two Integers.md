### Divide Two Integers

Divide two integers without using multiplication, division and mod operator.

If it is overflow, return MAX_INT.

[leetcode](https://leetcode.com/problems/divide-two-integers/description/)

### Answer

I x2 every time and reset the multiplier when exceed the target. Actually, we can also use binary search to solve this problem by detecting divisor * x <= diviend && divisor * (x+1) > diviend

	class Solution {
	public:
	    int divide(int dividend, int divisor) {
	        if (dividend == 0) return 0;
	        if (divisor == 0) return INT_MAX;
	        
	        long dd = dividend, dr = divisor;
	        long flag = (dd >= 0 && dr >= 0) || (dd <= 0 && dr <= 0) ? 1 : -1;
	        dd = dd >= 0 ? dd : -dd;
	        dr = dr >= 0 ? dr : -dr;
	        
	        long result = 0, base = 1;
	        while (dd >= dr)
	        {
	            long tmpDr = dr;
	            base = 1;
	            while (dd >= tmpDr)
	            {
	                dd -= tmpDr;
	                result += base;
	                base <<= 1;
	                tmpDr <<= 1;
	                if (flag*result > INT_MAX || flag*result < INT_MIN) return INT_MAX;
	            }
	        }
	        
	        return flag*result;
	    }
	};