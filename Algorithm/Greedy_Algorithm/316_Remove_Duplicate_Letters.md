### Remove Duplicate Letters
Given a string which contains only lowercase letters, remove duplicate letters so that every letter appear once and only once. You must make sure your result is the smallest in lexicographical order among all possible results.

Example:
Given "bcabc"
Return "abc"

Given "cbacdcbc"
Return "acdb"

[leetcode](https://leetcode.com/problems/remove-duplicate-letters/description/)

### Answer 
I like this problem. Give me new thought. We can use a stack, whenever meets a element larger than the elements in the stack, we can pop it out to minimize the lex order. BUT, we need to track if the pop out element still has remaining later. 

	class Solution {
	public:
	    string removeDuplicateLetters(string s) {
	        vector<int> counts(26, 0);
	        for (int i = 0; i < s.size(); ++i)
	        {
	            ++counts[s[i] - 'a'];
	        }
	        vector<bool> appear(26, false);
	        stack<char> myStk;
	        for (int i = 0; i < s.size(); ++i)
	        {
	            if (appear[s[i] - 'a']) 
	            {
	                --counts[s[i] - 'a'];
	                continue;
	            }
	            // pop out the guy larger than it and still have after it
	            while (!myStk.empty())
	            {
	                if (myStk.top() > s[i] && counts[myStk.top() - 'a'] > 0)
	                {
	                    appear[myStk.top() - 'a'] = false;
	                    myStk.pop();
	                }
	                else break;
	            }
	            myStk.push(s[i]);
	            --counts[s[i] - 'a'];
	            appear[s[i] - 'a'] = true;
	        }
	        
	        string result;
	        while (!myStk.empty())
	        {
	            result += myStk.top();
	            myStk.pop();
	        }
	        
	        reverse(result.begin(), result.end());
	        return result;
	    }
	};