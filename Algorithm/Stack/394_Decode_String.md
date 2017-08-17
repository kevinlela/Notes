### Decode String
Given an encoded string, return it's decoded string.

The encoding rule is: k[encoded_string], where the encoded_string inside the square brackets is being repeated exactly k times. Note that k is guaranteed to be a positive integer.

You may assume that the input string is always valid; No extra white spaces, square brackets are well-formed, etc.

Furthermore, you may assume that the original data does not contain any digits and that digits are only for those repeat numbers, k. For example, there won't be input like 3a or 2[4].

Examples:

s = "3[a]2[bc]", return "aaabcbc".
s = "3[a2[c]]", return "accaccacc".
s = "2[abc]3[cd]ef", return "abcabccdcdcdef".

[leetcode](https://leetcode.com/problems/decode-string/description/)

### Answer 

	class Solution {
	public:
	    string decodeString(string s) {
	        string num;
	        stack<pair<int, string>> stk;
	        stk.push({1, ""});
	        for (int i = 0; i < s.size(); ++i)
	        {
	            if (isdigit(s[i])) num += s[i];
	            else if (s[i] == '[')
	            {
	                stk.push({atoi(num.c_str()), ""});
	                num.clear();
	            }
	            else if (s[i] == ']')
	            {
	                string curr;
	                for (int i = 0; i < stk.top().first; ++i)
	                    curr += stk.top().second;
	                stk.pop();
	                stk.top().second += curr;
	            }
	            else stk.top().second += s[i];
	        }
	        
	        return stk.empty() ? "" : stk.top().second;
	    }
	};