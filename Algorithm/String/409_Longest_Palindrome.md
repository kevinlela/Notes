### Longest Palindrome
Given a string which consists of lowercase or uppercase letters, find the length of the longest palindromes that can be built with those letters.

This is case sensitive, for example "Aa" is not considered a palindrome here.

Note:
Assume the length of given string will not exceed 1,010.

Example:

Input:
"abccccdd"

Output:
7

Explanation:
One longest palindrome that can be built is "dccaccd", whose length is 7.


[leetcode](https://leetcode.com/submissions/detail/110612696/)

### Answer 
any >= 1 char can form parlindrom, and do allow one odd at middle. 

class Solution {
public:
    int longestPalindrome(string s) {
        int counts[52] = {0};
        for (int i = 0; i < s.size(); ++i)
        {
            int idx = s[i] >= 'a' ? (s[i] - 'a' + 26) : (s[i] - 'A');
            ++counts[idx];
        }
        
        bool odd = false;
        int len = 0;
        for (int i = 0; i < 52; ++i)
        {
            if (counts[i] % 2 == 1) odd = true;
            len += counts[i] / 2;
        }
        
        
        return odd ? (2*len + 1) : 2*len;
    }
};