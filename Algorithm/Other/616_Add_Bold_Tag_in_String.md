### Add Bold Tag in String
Given a string s and a list of strings dict, you need to add a closed pair of bold tag <b> and </b> to wrap the substrings in s that exist in dict. If two such substrings overlap, you need to wrap them together by only one pair of closed bold tag. Also, if two substrings wrapped by bold tags are consecutive, you need to combine them.

Example 1:
Input: 
s = "abcxyz123"
dict = ["abc","123"]
Output:
"<b>abc</b>xyz<b>123</b>"
Example 2:
Input: 
s = "aaabbcc"
dict = ["aaa","aab","bc"]
Output:
"<b>aaabbc</b>c"
Note:
The given dict won't contain duplicates, and its length won't exceed 100.
All the strings in input have length in range [1, 1000].

[leetcode](https://leetcode.com/problems/add-bold-tag-in-string/description/)

### Answer
This is the problem of merge interval. to optimize my current solution, I can use kmp to find substring from dict. How to use kmp? use the stl function string.find()

	class Solution {
	public:
	    string addBoldTag(string s, vector<string>& dict) {
	        unordered_set<string> hm;
	        int maxLen = 0;
	        for (int i = 0; i < dict.size(); ++i)
	        {
	            if (dict[i].size() <= s.size())
	            {
	                hm.insert(dict[i]);
	                maxLen = max(maxLen, (int)dict[i].size());
	            }
	        }
	        
	        int sLen = s.size();
	        vector<pair<int, int>> br;
	        for (int i = 0; i < s.size(); ++i)
	        {
	            for (int j = min(i + maxLen, sLen) - 1; j >= i; --j)
	            {
	                string sub = s.substr(i, j - i + 1);
	                if (hm.find(sub) != hm.end()) 
	                {
	                    br.push_back({i, j});
	                    break;
	                }
	            }
	        }
	        
	        if (br.size() == 0) return s;
	        
	        vector<pair<int, int>> mbr; // merge br
	        mbr.push_back(br[0]);
	        
	        for (int i = 1; i < br.size(); ++i)
	        {
	            //cout << br[i].first << ", " << br[i].second << endl;
	            if (br[i].first <= mbr.rbegin()->second + 1) 
	                mbr.rbegin()->second = max(br[i].second, mbr.rbegin()->second);
	            else
	                mbr.push_back(br[i]);
	        }
	        
	        int j = 0;
	        string result;
	        for (int i = 0; i < s.size(); ++i)
	        {
	            if (j < mbr.size() && i == mbr[j].first) result += "<b>";
	            result.append(1, s[i]);
	            if (j < mbr.size() && i == mbr[j].second)
	            {
	                result += "</b>";
	                ++j;
	            }
	        }
	        
	        return result;
	    }
	};