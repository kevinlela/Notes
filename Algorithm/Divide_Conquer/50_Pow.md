### Pow(x, n)
Implement pow(x, n).

[leetcode](https://leetcode.com/problems/powx-n/description/)

### Answer 
to compensate the odd use n*pow(x, n/2)

	class Solution {
	public:
	    double myPow(double x, int n) {
	        if (n < 0) return myPowL(1/x, -(long)n);
	        return myPowL(x, n);
	    }
	    
	    double myPowL(double x, long n)
	    {
	        if (n == 0) return 1;
	        if (x == 1) return 1;
	        if (x == 0) return 0;
	        
	        return n%2 == 0 ? myPow(x*x, n/2) : x*myPow(x*x, n/2);
	    }
	};