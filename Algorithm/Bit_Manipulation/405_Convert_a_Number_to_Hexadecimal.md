### Convert a Number to Hexadecimal
Given an integer, write an algorithm to convert it to hexadecimal. For negative integer, two’s complement method is used.

Note:

All letters in hexadecimal (a-f) must be in lowercase.
The hexadecimal string must not contain extra leading 0s. If the number is zero, it is represented by a single zero character '0'; otherwise, the first character in the hexadecimal string will not be the zero character.
The given number is guaranteed to fit within the range of a 32-bit signed integer.
You must not use any method provided by the library which converts/formats the number to hex directly.
Example 1:

Input:
26

Output:
"1a"
Example 2:

Input:
-1

Output:
"ffffffff"

[leetcode](https://leetcode.com/problems/convert-a-number-to-hexadecimal/description/)

### Answer 

	class Solution {
	public:
	    string toHex(int num) {
	        string result;
	        int len = 8;
	        while (num && len-- > 0)
	        {
	            int curr = (num & 0xf);
	            result += curr < 10 ? ('0' + curr) : ('a' + curr - 10);
	            num >>= 4;
	        }
	        
	        reverse(result.begin(), result.end());
	        return result.empty() ? "0" : result;
	    }
	};