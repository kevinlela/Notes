### Valid Perfect Square
Given a positive integer num, write a function which returns True if num is a perfect square else False.

Note: Do not use any built-in library function such as sqrt.

Example 1:

Input: 16
Returns: True
Example 2:

Input: 14
Returns: False

[leetcode](https://leetcode.com/problems/valid-perfect-square/description/)

### Answer
	class Solution {
	public:
	    bool isPerfectSquare(int num) {
	        if ( num < 0 ) return false;
	        if ( num == 1 || num == 4) return true;
	        if ( num == 2 || num == 3) return false;
	        int st = 3, ed = num/2 + 1;
	        while (st < ed)
	        {
	            int mid = st + (ed - st)/2;
	            long res = (long) mid * (long) mid;
	            if (res == num) return true;
	            else if (res < num) st = mid + 1;
	            else ed = mid;
	        }
	        
	        return false;
	    }
	};