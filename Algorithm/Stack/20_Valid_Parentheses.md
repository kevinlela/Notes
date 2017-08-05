### Valid Parentheses

Given a string containing just the characters '(', ')', '{', '}', '[' and ']', determine if the input string is valid.

The brackets must close in the correct order, "()" and "()[]{}" are all valid but "(]" and "([)]" are not.

[leetcode](https://leetcode.com/problems/valid-parentheses/description/)

### Answer:

It is very natural to think of using stack since the new coming one must match the most recent added one. 

	class Solution {
	public:
	    bool isValid(string s) {
	        stack<char> status;
	        for (int i = 0; i < s.size(); ++i)
	        {
	            if (s[i] == '(' || s[i] == '[' || s[i] == '{') status.push(s[i]);
	            else if (status.empty()) return false;
	            else if (s[i] == ')' && status.top() == '(') status.pop();
	            else if (s[i] == ']' && status.top() == '[') status.pop();
	            else if (s[i] == '}' && status.top() == '{') status.pop();
	            else return false;
	        }
	        return status.empty();
	    }
	};