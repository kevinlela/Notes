### Length of Last Word
Given a string s consists of upper/lower-case alphabets and empty space characters ' ', return the length of last word in the string.

If the last word does not exist, return 0.

Note: A word is defined as a character sequence consists of non-space characters only.

For example, 
Given s = "Hello World",
return 5.

[leetcode](https://leetcode.com/problems/length-of-last-word/description/)

### Answer 

	class Solution {
	public:
	    int lengthOfLastWord(string s) {
	        int i = 0, len = s.size();
	        for (i = len - 1; i >= 0; --i)
	        {
	            if (s[i] != ' ') break;
	        }
	        
	        int result = 0;
	        for (; i >= 0; --i)
	        {
	            if (s[i] == ' ') break;
	            ++result;
	        }
	        return result;
	    }
	};