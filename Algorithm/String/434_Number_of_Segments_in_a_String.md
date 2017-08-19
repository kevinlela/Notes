### Number of Segments in a String
Count the number of segments in a string, where a segment is defined to be a contiguous sequence of non-space characters.

Please note that the string does not contain any non-printable characters.

Example:

Input: "Hello, my name is John"
Output: 5

[leetcode](https://leetcode.com/problems/number-of-segments-in-a-string/description/)

### Answer 

	class Solution {
	public:
	    int countSegments(string s) {
	        bool inWord = false;
	        int result = 0;
	        for (int k = 0; k < s.size(); ++k)
	        {
	            if (s[k] != ' ' && inWord == false)
	            {
	                ++result;
	                inWord = true;
	            }
	            else if (s[k] == ' ' && inWord == true)
	            {
	                inWord = false;
	            }
	        }
	        return result;
	    }
	};