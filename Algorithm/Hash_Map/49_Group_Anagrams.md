### Group Anagrams
Given an array of strings, group anagrams together.

For example, given: ["eat", "tea", "tan", "ate", "nat", "bat"], 
Return:

[
  ["ate", "eat","tea"],
  ["nat","tan"],
  ["bat"]
]
Note: All inputs will be in lower-case.

[leetcode](https://leetcode.com/problems/group-anagrams/description/)

### Answer 
Use sort to compare anagram and use hashmap to store

	class Solution {
	public:
	    vector<vector<string>> groupAnagrams(vector<string>& strs) {
	        unordered_map<string, vector<string>> hmp;
	        for (int i = 0; i < strs.size(); ++i)
	        {
	            hmp[sortStr(strs[i])].push_back(strs[i]);
	        }
	        
	        vector<vector<string>> result;
	        for (auto iter = hmp.begin(); iter != hmp.end(); ++iter)
	        {
	            vector<string> rowResult;
	            vector<string>& row = iter->second;
	            for (auto iStr = row.begin(); iStr != row.end(); ++iStr)
	            {
	                rowResult.push_back(*iStr);
	            }
	            result.push_back(rowResult);
	        }
	        
	        return result;
	    }
	    
	    string sortStr(const string& str)
	    {
	        int counts[26] = {0};
	        for (int i = 0; i < str.size(); ++i)
	        {
	            ++counts[str[i] - 'a'];
	        }
	        string result;
	        for (int i = 0; i < 26; ++i)
	        {
	            result.append(counts[i], i + 'a');
	        }
	        return result;
	    }
	};