### License Key Formatting
Now you are given a string S, which represents a software license key which we would like to format. The string S is composed of alphanumerical characters and dashes. The dashes split the alphanumerical characters within the string into groups. (i.e. if there are M dashes, the string is split into M+1 groups). The dashes in the given string are possibly misplaced.

We want each group of characters to be of length K (except for possibly the first group, which could be shorter, but still must contain at least one character). To satisfy this requirement, we will reinsert dashes. Additionally, all the lower case letters in the string must be converted to upper case.

So, you are given a non-empty string S, representing a license key to format, and an integer K. And you need to return the license key formatted according to the description above.

Example 1:
Input: S = "2-4A0r7-4k", K = 4

Output: "24A0-R74K"

Explanation: The string S has been split into two parts, each part has 4 characters.
Example 2:
Input: S = "2-4A0r7-4k", K = 3

Output: "24-A0R-74K"

Explanation: The string S has been split into three parts, each part has 3 characters except the first part as it could be shorter as said above.

[leetcode](https://leetcode.com/problems/license-key-formatting/description/)

### Answer
Easy to know the first group and then just evenly divide the rest

	class Solution {
	public:
	    string licenseKeyFormatting(string S, int K) {
	        int len = S.size();
	        string result;
	        int fs = 0, nc = 0;
	        for (int i = 0 ; i < len; ++i)
	        {
	            if (S[i] == '-') continue;
	            ++nc;
	        }
	        fs = nc % K;
	        int i = 0; 
	        for (i = 0; i < len && fs > 0; ++i)
	        {
	            if (S[i] == '-') continue;
	            result.push_back(toupper(S[i]));
	            --fs;
	            if (fs == 0) result.push_back('-');
	        }
	        
	        int gc = K;
	        for (; i < len; ++i)
	        {
	            if (S[i] == '-') continue;
	            result.push_back(toupper(S[i]));
	            --gc;
	            if (gc == 0) 
	            {
	                gc = K;
	                result.push_back('-');
	            }
	        }
	        
	        result.pop_back();
	        return result;
	    }
	};