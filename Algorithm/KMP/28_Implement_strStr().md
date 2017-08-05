### Implement strStr()

Implement strStr().

Returns the index of the first occurrence of needle in haystack, or -1 if needle is not part of haystack.

[leetcode](https://leetcode.com/problems/implement-strstr/description/)

### Answer

The optimal solution is to use kmp but I use brutal force this time, need to revisit

	class Solution {
	public:
	    int strStr(string haystack, string needle) {
	        if (needle.size() == 0) return 0;
	        if (needle.size() > haystack.size()) return -1;
	        
	        for (int i = 0; i <= haystack.size() - needle.size(); ++i)
	        {
	            int j = 0;
	            for (int k = i; j < needle.size(); ++k, ++j)
	            {
	                if (haystack[k] != needle[j]) break;
	            }
	            if(j == needle.size()) return i;
	        }
	        
	        return -1;
	    }
	};