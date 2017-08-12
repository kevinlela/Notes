### Compare Version Numbers
Compare two version numbers version1 and version2.
If version1 > version2 return 1, if version1 < version2 return -1, otherwise return 0.

You may assume that the version strings are non-empty and contain only digits and the . character.
The . character does not represent a decimal point and is used to separate number sequences.
For instance, 2.5 is not "two and a half" or "half way to version three", it is the fifth second-level revision of the second first-level revision.

Here is an example of version numbers ordering:

0.1 < 1.1 < 1.2 < 13.37

[leetcode](https://leetcode.com/problems/compare-version-numbers/description/)

### Answer 
A corner case worthy to note is that 1.0.0 and 1.0

	class Solution {
	public:
	    int compareVersion(string version1, string version2) {
	        int iter1 = 0, iter2 = 0, 
	            len1 = version1.size(), len2 = version2.size();
	        
	        while (iter1 < len1 || iter2 < len2)
	        {
	            int v1 = 0, v2 = 0;
	            
	            if (iter1 < len1)
	            {
	                int st1 = iter1; 
	                for (; iter1 < len1; ++iter1)
	                {
	                    if (version1[iter1] == '.') break;
	                }
	                v1 = stoi(version1.substr(st1, iter1 - st1));
	            }
	            
	            if (iter2 < len2)
	            {
	                int st2 = iter2;
	                for (; iter2 < len2; ++iter2)
	                {
	                    if (version2[iter2] == '.') break;
	                }
	                v2 = stoi(version2.substr(st2, iter2 - st2));
	            }
	            
	            if (v1 < v2) return -1;
	            if (v1 > v2) return 1;
	            ++iter1;
	            ++iter2;
	        }
	        
	        return 0;
	    }
	};