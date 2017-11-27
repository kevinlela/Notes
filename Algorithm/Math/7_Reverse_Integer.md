### Reverse Integer

Reverse digits of an integer.

Example1: x = 123, return 321
Example2: x = -123, return -321

[leetcode](https://leetcode.com/problems/reverse-integer/description/)

### Answer
Meet this kind of problem, which is very easy to think through, always think about the corner cases

* what about 1000?
* what about negative case?
* what about overflow?
-------------------------------

	class Solution {
	public:
	    int reverse(int x) {
	        long xL = x < 0 ? -x : x;
	        long fL = x < 0 ? -1 : 1;
	        long res = 0;
	        
	        while (xL > 0)
	        {
	            res = res*10 + xL%10;
	            xL /= 10;
	        }
	        
	        res *= fL;
	        
	        return (res > INT_MAX || res < INT_MIN) ? 0 : res; 
	    }
	};