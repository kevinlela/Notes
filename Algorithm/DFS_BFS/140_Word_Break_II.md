### Word Break II
Given a non-empty string s and a dictionary wordDict containing a list of non-empty words, add spaces in s to construct a sentence where each word is a valid dictionary word. You may assume the dictionary does not contain duplicate words.

Return all such possible sentences.

For example, given
s = "catsanddog",
dict = ["cat", "cats", "and", "sand", "dog"].

A solution is ["cats and dog", "cat sand dog"].

UPDATE (2017/1/4):
The wordDict parameter had been changed to a list of strings (instead of a set of strings). Please reload the code definition to get the latest changes.

[leetcode](https://leetcode.com/problems/word-break-ii/description/)

### Answer 
It is a very simple dfs problem but just use dp to avoid wasted search for invalid input. 

	class Solution {
	public:
	    vector<string> wordBreak(string s, vector<string>& wordDict) {
	        vector<string> result;
	        unordered_set<string> wd;
	        set<int> lens;
	        
	        if (!isWordBreak(s, wordDict, wd, lens)) return result;
	        
	        recur(result, "", s, 0, wd);
	        return result;
	    }
	    
	    void recur(vector<string> &result, string path, const string &s, int curr, 
	               const unordered_set<string> &wd)
	    {
	        int len = s.size();
	        
	        if (curr >= len)
	        {
	            path.pop_back();
	            result.push_back(path);
	            return;
	        }
	        
	        string possibleWord;
	        for (int l = 0; l + curr < len; ++l)
	        {
	            possibleWord.append(1, s[l+curr]);
	            path.append(1, s[l+curr]);
	            
	            if (wd.find(possibleWord) != wd.end()) 
	            {
	                recur(result, path + " ", s, curr + l + 1, wd);
	            }
	        }
	    }
	    
	    bool isWordBreak(const string &s, const vector<string>& wordDict, 
	                     unordered_set<string> &wd, set<int> &lens) 
	    {
	        int sLen = s.size();
	        
	        for (auto iter = wordDict.begin(); iter != wordDict.end(); ++iter)
	        {
	            if (iter->size() > sLen) continue;
	            lens.insert(iter->size());
	            wd.insert(*iter);
	        }
	        
	        
	        if (sLen == 0) return false;
	        
	        vector<bool> dp(sLen - 1, false);
	        dp[0] = true;
	        
	        for (int k = 1; k <= sLen; ++k)
	        {
	            for (auto iter = lens.begin(); (*iter) <= k && iter != lens.end(); ++iter)
	            {
	                if (wd.find(s.substr(k - *iter, *iter)) != wd.end())
	                {
	                    dp[k] = dp[k - *iter];
	                }
	                if (dp[k]) break;
	            }
	        }
	        
	        return dp[sLen];
	    }
	};