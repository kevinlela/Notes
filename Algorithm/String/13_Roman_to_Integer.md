### Roman to Integer

Given a roman numeral, convert it to an integer.

Input is guaranteed to be within the range from 1 to 3999.

[leetcode](https://leetcode.com/problems/roman-to-integer/description/)

### Answer:

Solving from back of the string is easier than from the front of the string. 

	class Solution {
	public:
	    int romanToInt(string s) {
	        unordered_map<char, int> r2i = {{'I', 1}, {'V', 5}, {'X', 10}, {'L', 50},
	                                        {'C', 100}, {'D', 500}, {'M', 1000}};
	        char curChar = 'I';
	        int result = 0;
	        for (int i = s.size(); i > 0; )
	        {
	            --i;
	            if (r2i[s[i]] < r2i[curChar]) result -= r2i[s[i]];
	            else 
	            {
	                result += r2i[s[i]];
	                curChar = s[i];
	            }
	        }
	        return result;
	    }
	};

