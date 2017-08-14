### Isomorphic Strings
Given two strings s and t, determine if they are isomorphic.

Two strings are isomorphic if the characters in s can be replaced to get t.

All occurrences of a character must be replaced with another character while preserving the order of characters. No two characters may map to the same character but a character may map to itself.

For example,
Given "egg", "add", return true.

Given "foo", "bar", return false.

Given "paper", "title", return true.

Note:
You may assume both s and t have the same length.

[leetcode](https://leetcode.com/problems/isomorphic-strings/description/)

### Answer 

	class Solution {
	public:
	    bool isIsomorphic(string s, string t) {
	        unordered_map<char, char> s2t;
	        unordered_map<char, char> t2s;
	        
	        int len = t.size();
	        
	        for (int i = 0; i < len; ++i)
	        {
	            if (s2t.find(s[i]) == s2t.end() && t2s.find(t[i]) == t2s.end())
	            {
	                s2t[s[i]] = t[i];
	                t2s[t[i]] = s[i];
	            }
	            else if (   s2t.find(s[i]) != s2t.end() 
	                     && t2s.find(t[i]) != t2s.end() )
	            {
	                if (s2t[s[i]] != t[i] || t2s[t[i]] != s[i]) return false;
	            }
	            else return false;
	        }
	        return true;
	    }
	};