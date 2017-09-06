### Reverse String II
Given a string and an integer k, you need to reverse the first k characters for every 2k characters counting from the start of the string. If there are less than k characters left, reverse all of them. If there are less than 2k but greater than or equal to k characters, then reverse the first k characters and left the other as original.
Example:
Input: s = "abcdefg", k = 2
Output: "bacdfeg"
Restrictions:
The string consists of lower English letters only.
Length of the given string and k will in the range [1, 10000]

[leetcode](https://leetcode.com/problems/reverse-string-ii/description/)

### Answer

	class Solution {
	public:
	    string reverseStr(string s, int k) {
	        int st = 0, ed = k;
	        int len = s.size();
	        while (st < len)
	        {
	            reverse(s.begin() + st, s.begin() + min(ed, len));
	            st += 2*k;
	            ed = st + k;
	        }
	        
	        return s;
	    }
	};