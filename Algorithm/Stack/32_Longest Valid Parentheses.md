### Longest Valid Parentheses

Given a string containing just the characters '(' and ')', find the length of the longest valid (well-formed) parentheses substring.

For "(()", the longest valid parentheses substring is "()", which has length = 2.

Another example is ")()())", where the longest valid parentheses substring is "()()", which has length = 4.

[leetcode](https://leetcode.com/problems/longest-valid-parentheses/description/)

### Answer 

Use a stack and record the status of ( and ), then we just need to count the longest consecutive 1

	class Solution {
	public:
	    int longestValidParentheses(string s) {
	        stack<int> stk;
	        vector<bool> valid(s.length(), false);
	        
	        for (int i = 0; i < s.length(); ++i)
	        {
	            if (s[i] == '(') stk.push(i);
	            else if (!stk.empty())
	            {
	                valid[stk.top()] = true;
	                valid[i] = true;
	                stk.pop();
	            }
	        }
	        
	        int len = 0, resLen = 0;
	        for (int i = 0; i < valid.size(); ++i)
	        {
	            if (valid[i]) resLen = max(resLen, ++len);
	            else len = 0;
	        }
	        
	        return resLen;
	    }
	};

