### Reverse Words in a String III
Given a string, you need to reverse the order of characters in each word within a sentence while still preserving whitespace and initial word order.

Example 1:
Input: "Let's take LeetCode contest"
Output: "s'teL ekat edoCteeL tsetnoc"

[leetcode](https://leetcode.com/problems/reverse-words-in-a-string-iii/description/)

### Answer
	class Solution {
	public:
	    string reverseWords(string s) {
	        s += " ";
	        int st = -1;
	        for (int i = 0; i < s.size(); ++i)
	        {
	            if (s[i] == ' ') 
	            {
	                if (st != -1) reverse(s.begin() + st, s.begin() + i);
	                st = -1;
	            }
	            else if (st == -1) st = i;
	        }
	        s.pop_back();
	        return s;
	    }
	};