### Longest Common Prefix

Write a function to find the longest common prefix string amongst an array of strings.

[leetcode](https://leetcode.com/problems/longest-common-prefix/description/)

### Answer

	class Solution {
	public:
	    string longestCommonPrefix(vector<string>& strs) {
	        string result;
	        if (strs.size() == 0) return result;
	        
	        int i = 0;
	        while (1)
	        {
	            if (i >= strs[0].size()) return result;
	            char currChar = strs[0][i];
	            for (int j = 0; j < strs.size(); ++j)
	            {
	                if (i >= strs[j].size()) return result;
	                if (currChar != strs[j][i]) return result;
	            }
	            result += currChar;
	            ++i;
	        }
	        
	        return result;
	    }
	};