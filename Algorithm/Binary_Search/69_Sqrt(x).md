### Sqrt(x)

Implement int sqrt(int x).

Compute and return the square root of x.

[leetcode](https://leetcode.com/problems/sqrtx/description/)

### Answer 
what if float? use an absolute diff to track. |x^2 - t| < \epsilon. 

	class Solution {
	public:
	    int mySqrt(int x) {
	        long st = 0, ed = (long)x + 1;
	        while (st < ed)
	        {
	            long mid = st + (ed - st) / 2;
	            long res = mid*mid;
	            if (res == x) return mid;
	            else if (res > x) ed = mid;
	            else st = mid + 1;
	        }
	        
	        return ed - 1;
	    }
	};