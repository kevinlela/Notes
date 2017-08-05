### Palindrome Number

Determine whether an integer is a palindrome. Do this without extra space.

[leetcode](https://leetcode.com/problems/palindrome-number/description/)

### Answer
Do we need to traverse the whole number? NO. the length of a number can be either odd or even, the first half A and reverse the second half B. if parlindrome, only two cases A == B or A/10 == B. So, we only need to compare half length of number

Corner Case
* 10000
* negative number

	class Solution {
	public:
	    bool isPalindrome(int x) {
	        if (x < 0) return false;
	        int xL = x, right = 0;
	        
	        //exclude for 1000000
	        if (xL == 0) return true;
	        if (xL % 10 == 0) return false;
	        
	        while (right < xL)
	        {
	            if (xL / 10 == right) return true;
	            right = 10 * right + xL % 10;
	            xL /= 10;
	            if (xL == right) return true;
	        }
	        
	        return false;
	    }
	};


