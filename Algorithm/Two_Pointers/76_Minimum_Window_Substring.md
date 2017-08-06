### Minimum Window Substring
Given a string S and a string T, find the minimum window in S which will contain all the characters in T in complexity O(n).

For example,
S = "ADOBECODEBANC"
T = "ABC"
Minimum window is "BANC".

Note:
If there is no such window in S that covers all characters in T, return the empty string "".

If there are multiple such windows, you are guaranteed that there will always be only one unique minimum window in S.

[leetcode](https://leetcode.com/problems/minimum-window-substring/description/)

### Answer 
Two pointers problem usually, maintain a window, once it is valid, make it invalid

class Solution {
public:
    string minWindow(string s, string t) {
        unordered_map<char, int> counts;
        int tLen = t.size();
        for (int i = 0; i < tLen; ++i)
        {
            ++counts[t[i]];
        }
        
        int lastPt = 0, minWin = -1, resSt = -1;
        for (int i = 0; i < s.size(); ++i)
        {
            if (counts.find(s[i]) == counts.end()) continue;
            else
            {
                --counts[s[i]];
                if (counts[s[i]] >= 0) --tLen;
                if (tLen == 0) // satisfy
                {
                	//make the window invalid
                    for (; lastPt <= i; ++lastPt)
                    {
                        if (counts.find(s[lastPt]) == counts.end()) continue;
                        ++counts[s[lastPt]];
                        if (counts[s[lastPt]] > 0)
                        {
                            ++tLen;
                            break;
                        }
                    }
                    
                    int currWin = i - lastPt + 1;
                    if (minWin == -1 || minWin > currWin)
                    {
                        minWin = currWin;
                        resSt = lastPt;
                    }
                    
                    ++lastPt;
                }
            }
        }
        
        return resSt == -1 ? "" : s.substr(resSt, minWin);
    }
};