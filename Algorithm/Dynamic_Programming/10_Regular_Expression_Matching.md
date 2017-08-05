### Regular Expression Matching

Implement regular expression matching with support for '.' and '*'.

	'.' Matches any single character.
	'*' Matches zero or more of the preceding element.

	The matching should cover the entire input string (not partial).

	The function prototype should be:
	bool isMatch(const char *s, const char *p)

	Some examples:
	isMatch("aa","a") ? false
	isMatch("aa","aa") ? true
	isMatch("aaa","aa") ? false
	isMatch("aa", "a*") ? true
	isMatch("aa", ".*") ? true
	isMatch("ab", ".*") ? true
	isMatch("aab", "c*a*b") ? true

### Answer:
First, clean the input. 
* consecutive \* makes no sense, we can shrink them into one

Second, define the dp. dp[i][j] represents s[0...i] matches p[0...j] or not. There are three cases
* s[i] is normal char, so dp[i][j] = dp[i-1][j-1] && s[i] == p[j]
* s[i] == '.', so dp[i][j] = dp[i-1][j-1]
* s[i] == '*', this one depend on preceding element
	* s[i-1] == normal char
		* zero preceding dp[i-1][j]
		* non-zero preceding dp[i-1][j-1] && s[i-1] == p[j]
	* s[i-1] == '.'
		* zero preceding dp[i-1][j]
		* non-zero preceding dp[i-1][j-1]

	class Solution {
	public:
	    bool isMatch(string s, string p) {
	        // only p has * and .
	        // first, leading * means nothing because we do not have preceding element
	        // remove leading *
	        // Second, consecutive * means nothing, we can reduce them into one
	        p = cutUselessStar(p);
	        
	        int len1 = s.size(), len2 = p.size();
	        
	        // let dp[i][j] represent if s[0...i] and p[0...j] is matched or not
	        // it depends on 3 cases:
	        // if p[j] is character: dp[i-1][j-1] == true && s[i] == p[j]
	        // if p[j] is '.' : dp[i-1][j-1] == true
	        // if p[j] is '*' : dp[i][j-2] (delete preceding) || dp[i][j-1] (means nothing) || (dp[i-1][j] && s[i] == p[j-1])
	        vector<vector<bool>> dp(len1 + 1, vector<bool>(len2 + 1, false));
	        
	        // empty s matches empty t
	        dp[0][0] = true;
	        
	        // s will not match empty p so the first column is all false;
	        if (s[0] == p[0] || p[0] == '.') dp[0][0] = true;
	        
	        // match p with empty s
	        for (int j = 1; j <= len2; ++j)
	        {
	            if (p[j-1] == '*') dp[0][j] = dp[0][j-2] || dp[0][j-1];
	        }
	        
	        // match p and s
	        for (int i = 1; i <= len1; ++i)
	        {
	            for (int j = 1; j <= len2; ++j)
	            {
	                if (p[j-1] == '.')
	                {
	                    if (dp[i-1][j-1]) dp[i][j] = true;
	                }
	                else if (p[j-1] == '*')
	                {
	                    if (dp[i][j-2]) dp[i][j] = true; //delete including preceding character
	                    else if (dp[i][j-1]) dp[i][j] = true; //delete * only
	                    else if (dp[i-1][j])
	                    {
	                        if (s[i-1] == p[j-2] || p[j-2] == '.') dp[i][j] = true; // repeat previous one
	                    }
	                }
	                else if (p[j-1] == s[i-1]) dp[i][j] = dp[i-1][j-1];
	            }
	        }
	        
	        return dp[len1][len2];
	    }
	    
	    string cutUselessStar(string &inStr)
	    {
	        string result;
	        int i = 0;
	        
	        //remove leading star
	        for (; i < inStr.size(); ++i)
	        {
	            if (inStr[i] != '*') break;
	        }
	        if (i == inStr.size()) return result;
	        
	        //reduce consecutive stars to single one
	        for (; i < inStr.size(); ++i)
	        {
	            if (result.empty() || inStr[i] != '*') result += inStr[i];
	            else if (*(result.rbegin()) != '*') result += inStr[i];
	        }
	        
	        return result;
	    }
	};