### Longest Word in Dictionary through Deleting
Given a string and a string dictionary, find the longest string in the dictionary that can be formed by deleting some characters of the given string. If there are more than one possible results, return the longest word with the smallest lexicographical order. If there is no possible result, return the empty string.

Example 1:
Input:
s = "abpcplea", d = ["ale","apple","monkey","plea"]

Output: 
"apple"
Example 2:
Input:
s = "abpcplea", d = ["a","b","c"]

Output: 
"a"
Note:
All the strings in the input will only contain lower-case letters.
The size of the dictionary won't exceed 1,000.
The length of all the strings in the input won't exceed 1,000.

[leetcode](https://leetcode.com/problems/longest-word-in-dictionary-through-deleting/description/)

### Answer
Sort the array by lex order and detet one by one

	class Solution {
	public:
	    struct cmp{
	        inline bool operator () (const string &s1, const string &s2)
	        {
	            if (s1.size() == s2.size()) return s1 < s2;
	            return s1.size() > s2.size();
	        }
	    };
	    
	    string findLongestWord(string s, vector<string>& d) {
	        sort(d.begin(), d.end(), cmp());
	        for (int i = 0; i < d.size(); ++i)
	        {
	            if (isSubStr(s, d[i])) return d[i];
	        }
	        return "";
	    }
	    
	    bool isSubStr(const string &l, const string &s)
	    {
	        int iter = 0;
	        for (int i = 0; i < l.size(); ++i)
	        {
	            if (s[iter] == l[i]) ++iter;
	        }
	        return iter == s.size();
	    }
	};