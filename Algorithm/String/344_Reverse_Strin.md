### Reverse Strin
Write a function that takes a string as input and returns the string reversed.

Example:
Given s = "hello", return "olleh".

[leetcode](https://leetcode.com/problems/reverse-string/description/)

### Answer 

	class Solution {
	public:
	    string reverseString(string s) {
	        reverse(s.begin(), s.end());
	        return s;
	    }
	};