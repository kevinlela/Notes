### Nth Digit
Find the nth digit of the infinite integer sequence 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, ...

Note:
n is positive and will fit within the range of a 32-bit signed integer (n < 231).

Example 1:

Input:
3

Output:
3
Example 2:

Input:
11

Output:
0

Explanation:
The 11th digit of the sequence 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, ... is a 0, which is part of the number 10.

[leetcode](https://leetcode.com/problems/nth-digit/description/)

### Answer 
This problem is not hard but need clear strategy, we first calculate what is the target number. and then calculate which digit. 

	class Solution {
	public:
	    int findNthDigit(int n) {
	        if (n < 10) return n;
	        int digits = 1;
	        long count = 9, base = 9, st = 1;
	        while (count < n)
	        {
	            ++digits;
	            base *= 10;
	            count += base * digits;
	            st *= 10;
	        }
	        
	        long prev = count - base*digits + 1;
	        
	        // decide which one
	        int real = (n - prev)/digits + st;
	        
	        // decide which digit
	        int nth = (n - prev) % digits;
	        
	        //cout << real << " " << nth << endl;
	        int result = 0;
	        for (int i = 0; i < digits - nth; ++i)
	        {
	            result = real % 10;
	            real /= 10;
	        }
	        return result;
	    }
	};