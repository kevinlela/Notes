### First Unique Character in a String
Given a string, find the first non-repeating character in it and return it's index. If it doesn't exist, return -1.

Examples:

s = "leetcode"
return 0.

s = "loveleetcode",
return 2.

[leetcode](https://leetcode.com/problems/first-unique-character-in-a-string/description/)

### Answer 

	class Solution {
	public:
	    int firstUniqChar(string s) {
	        int counts[256] = {0};
	        for (int i = 0; i < s.size(); ++i)
	        {
	            ++counts[s[i]];
	        }
	        
	        for (int i = 0; i < s.size(); ++i)
	        {
	            if (counts[s[i]] == 1) return i;
	        }
	        return -1;
	    }
	};