### Count Numbers with Unique Digits
Given a non-negative integer n, count all numbers with unique digits, x, where 0 ≤ x < 10^n.

Example:
Given n = 2, return 91. (The answer should be the total numbers in the range of 0 ≤ x < 100, excluding [11,22,33,44,55,66,77,88,99])


[leetcode](https://leetcode.com/problems/count-numbers-with-unique-digits/description/)

### Answer
This has a trap that if you want to use rule checking by enumerating case, this is actually a combination problem. When you pick a digit, there is (n-1)! ways. Notice the 0, so the first digits only has 9 choices, and the second also start at 9 choices. 

	class Solution {
	public:
	    int countNumbersWithUniqueDigits(int n) {
	        if (n == 0) return 1;
	        if (n == 1) return 10;
	        int res = 10;
	        int p = 9;
	        if (n > 9) n = 9;
	        int m = 9;
	        while (n > 1)
	        {
	            res += 9*p;
	            --n;
	            p *= (--m);
	        }
	        return res;
	    }
	};