### Group Shifted Strings
Given a string, we can "shift" each of its letter to its successive letter, for example: "abc" -> "bcd". We can keep "shifting" which forms the sequence:

"abc" -> "bcd" -> ... -> "xyz"
Given a list of strings which contains only lowercase alphabets, group all strings that belong to the same shifting sequence.

For example, given: ["abc", "bcd", "acef", "xyz", "az", "ba", "a", "z"], 
A solution is:

[
  ["abc","bcd","xyz"],
  ["az","ba"],
  ["acef"],
  ["a","z"]
]

[leetcode](https://leetcode.com/problems/group-shifted-strings/description/)

### Answer
	class Solution {
	public:
	    vector<vector<string>> groupStrings(vector<string>& strings) {
	        unordered_map<string, int> words;
	        for (int i = 0; i < strings.size(); ++i)
	            ++words[strings[i]];
	        
	        vector<vector<string>> result;
	        for (int i = 0; i < strings.size(); ++i)
	        {
	            vector<string> line;
	            if (words.find(strings[i]) == words.end()) continue;
	            for (int j = 0; j < 26; ++j)
	            {
	                auto it = words.find(strings[i]);
	                if (it != words.end())
	                {
	                    line.insert(line.end(), it->second, strings[i]);
	                    words.erase(it);
	                }
	                shift(strings[i]);
	            }
	            result.push_back(line);
	        }
	        return result;
	    }
	    
	    void shift(string &in)
	    {
	        int len = in.size();
	        for (int i = 0; i < len; ++i)
	        {
	            ++in[i];
	            if (in[i] > 'z') in[i] = 'a';
	        }
	    }
	    
	    
	};