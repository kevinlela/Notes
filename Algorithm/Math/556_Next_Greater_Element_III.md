### Next Greater Element III
Given a positive 32-bit integer n, you need to find the smallest 32-bit integer which has exactly the same digits existing in the integer n and is greater in value than n. If no such positive 32-bit integer exists, you need to return -1.

Example 1:
Input: 12
Output: 21
Example 2:
Input: 21
Output: -1

[leetcode](https://leetcode.com/problems/next-greater-element-iii/description/)

### Answer
This problem is similar with [31_Next_Permutation](31_Next_Permutation.md).

class Solution {
public:
    int nextGreaterElement(int n) {
        string maxN = "2147483647";
        string strN = to_string(n);
        int len = strN.size();
        if (len == 1 || len == 0) return -1;
        
        int i = len - 2;
        for (i; i >= 0; --i)
        {
            if (strN[i] < strN[i+1]) break;
        }
        
        if (i < 0) return -1; // already the largest
        
        int k = len - 1;
        for (k; k > i; --k)
        {
            if (strN[k] > strN[i]) break;
        }
        
        swap(strN[i], strN[k]);
        reverse(strN.begin() + i + 1, strN.end());
        
        if (strN.size() == maxN.size() && strN > maxN) return -1;
        return atoi(strN.c_str());
    }
};
