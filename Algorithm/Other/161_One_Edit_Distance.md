### One Edit Distance
Given two strings S and T, determine if they are both one edit distance apart.

[leetcode](https://leetcode.com/problems/one-edit-distance/description/)

### Answer

	class Solution {
	public:
	    bool isOneEditDistance(string s, string t) {
	        // the operation is change, insert or delete
	        int iter1 = 0, iter2 = 0;
	        int sLen = s.size(), tLen = t.size();
	        if (abs(sLen - tLen) >= 2) return false;
	        
	        bool inTrouble = false;
	        
	        while (iter1 < sLen || iter2 < tLen)
	        {
	            if (iter1 >= sLen || iter2 >= tLen || s[iter1] != t[iter2])
	            {
	                if (inTrouble) return false;
	                else if (sLen == tLen) // only change could happen
	                {
	                    ++iter1;
	                    ++iter2;
	                }
	                else if (sLen > tLen) ++iter1; // only delete
	                else ++iter2; // only insert
	                inTrouble = true;
	            }
	            else
	            {
	                ++iter1;
	                ++iter2;
	            }
	        }
	        
	        return inTrouble && (iter1 >= sLen) && (iter2 >= tLen);
	    }
	};