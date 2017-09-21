### Reverse Words in a String II
Given an input string, reverse the string word by word. A word is defined as a sequence of non-space characters.

The input string does not contain leading or trailing spaces and the words are always separated by a single space.

For example,
Given s = "the sky is blue",
return "blue is sky the".

Could you do it in-place without allocating extra space?

[leetcode](https://leetcode.com/problems/reverse-words-in-a-string-ii/description/)

### Answer

	class Solution {
	public:
	    void reverseWords(string &s) {
	        if (s.empty()) return;
	        reverse(s.begin(), s.end());
	        int st = 0;
	        for (int i = 0; i < s.size(); ++i)
	        {
	            if (s[i] == ' ')
	            {
	                reverse(s.begin() + st, s.begin() + i);
	                st = i+1;
	            }
	        }
	        
	        reverse(s.begin() + st, s.end());
	    }
	};