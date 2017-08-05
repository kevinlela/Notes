### String to Integer (atoi)

Implement atoi to convert a string to an integer.

Hint: Carefully consider all possible input cases. If you want a challenge, please do not see below and ask yourself what are the possible input cases.

Notes: It is intended for this problem to be specified vaguely (ie, no given input specs). You are responsible to gather all the input requirements up front.

[leetcode](https://leetcode.com/problems/string-to-integer-atoi/description/)

Answer:
Corner cases
* sign
* overfollow
* leading and tailing space
* something like 1e2
* decimal

	class Solution {
	public:
	    int myAtoi(string str) {
	        // what do we return if the string is invalid? 0?
	        // string type:
	        // normal: 123
	        // leading zero: 0000123
	        // decimal: 123.123
	        // e: 1e5 -> 10000
	        // leading and tailing space *
	        // sign: "+" and "-"
	        long result = 0;
	        long fL = 1;
	        int i = 0;
	        
	        // skip space
	        for (; i < str.size(); ++i)
	        {
	            if (str[i] != ' ') break;
	        }
	        
	        if (i >= str.size())
	        {
	            return result;
	        }
	        
	        // check the start sign
	        if (str[i] == '+' || str[i] == '-')
	        {
	            fL = str[i] == '-' ? -1 : 1;
	            ++i;
	        }
	        
	        // check the body
	        for (; i < str.size(); ++i)
	        {
	            if (!isdigit(str[i])) break;
	            result = 10*result + (long)(str[i] - '0');
	            long resF = result * fL;
	            if (resF < INT_MIN) return INT_MIN;
	            if (resF > INT_MAX) return INT_MAX;
	        }
	        
	        return result * fL;
	    }
	};