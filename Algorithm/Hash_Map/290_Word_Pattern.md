### Word Pattern
Given a pattern and a string str, find if str follows the same pattern.

Here follow means a full match, such that there is a bijection between a letter in pattern and a non-empty word in str.

Examples:
pattern = "abba", str = "dog cat cat dog" should return true.
pattern = "abba", str = "dog cat cat fish" should return false.
pattern = "aaaa", str = "dog cat cat dog" should return false.
pattern = "abba", str = "dog dog dog dog" should return false.
Notes:
You may assume pattern contains only lowercase letters, and str contains lowercase letters separated by a single space.

[leetcode](https://leetcode.com/problems/word-pattern/description/)

### Answer

	class Solution {
	public:
	    bool wordPattern(string pattern, string str) {
	        unordered_map<char, string> p2s;
	        unordered_map<string, char> s2p;
	        
	        vector<string> words;
	        string word;
	        for (int i = 0; i < str.size(); ++i)
	        {
	            if (str[i] == ' ') 
	            {
	                words.push_back(word);
	                word.clear();
	            }
	            else word.append(1, str[i]);
	        }
	        if (!word.empty()) words.push_back(word);
	        
	        if (pattern.size() != words.size()) return false;
	        
	        for (int i = 0; i < pattern.size(); ++i)
	        {
	            auto p2sIter = p2s.find(pattern[i]);
	            auto s2pIter = s2p.find(words[i]);
	            if (p2sIter == p2s.end() && s2pIter == s2p.end())
	            {
	                p2s[pattern[i]] = words[i];
	                s2p[words[i]] = pattern[i];
	            }
	            else if (p2sIter != p2s.end() &&
	                     s2pIter != s2p.end())
	            {
	                if (p2s[pattern[i]] != words[i]) return false;
	                if (s2p[words[i]] != pattern[i]) return false;
	            }
	            else return false;
	        }
	        return true;
	    }
	};