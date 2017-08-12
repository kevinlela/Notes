### Excel Sheet Column Number
Related to question Excel Sheet Column Title

Given a column title as appear in an Excel sheet, return its corresponding column number.

For example:

    A -> 1
    B -> 2
    C -> 3
    ...
    Z -> 26
    AA -> 27
    AB -> 28 

[leetcode](https://leetcode.com/problems/excel-sheet-column-number/description/)

### Answer 

	class Solution {
	public:
	    int titleToNumber(string s) {
	        int len = s.size();
	        int result = 0;
	        for (int k = 0; k < len; ++k)
	        {
	            result *= 26;
	            result += s[k] - 'A' + 1;
	        }
	        return result;
	    }
	};