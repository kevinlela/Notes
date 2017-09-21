### Palindrome Permutation II
Given a string s, return all the palindromic permutations (without duplicates) of it. Return an empty list if no palindromic permutation could be form.

For example:

Given s = "aabb", return ["abba", "baab"].

Given s = "abc", return [].

[leetcode](https://leetcode.com/problems/palindrome-permutation-ii/description/)

### Answer
	class Solution {
	public:
	    vector<string> generatePalindromes(string s) {
	        // generate half
	        vector<string> result;
	        if (s.empty()) return result;
	        unordered_map<char, int> count;
	        for (int i = 0; i < s.size(); ++i)
	            ++count[s[i]];
	        
	        int odd = 0;
	        char odd_char = 0;
	        for (auto iter = count.begin(); iter != count.end(); ++iter)
	        {
	            if (iter->second % 2)
	            {
	                if (odd == 1) return result; 
	                ++odd;
	                iter->second = (iter->second - 1)/2;
	                odd_char = iter->first;
	            }
	            else iter->second /= 2;
	        }
	        
	        string curr;
	        int len = s.size();
	        if (len == 1)
	        {
	            result.push_back(s);
	            return result;
	        }
	        len = odd ? ((len-1)/2) : (len/2);
	        recur(result, count, curr, len);
	        
	        string center = odd ? string(1, odd_char) : "";
	        for (int i = 0; i < result.size(); ++i)
	        {
	            string right = result[i];
	            reverse(right.begin(), right.end());
	            result[i] += center + right;
	        }
	        return result;
	    }
	    
	    void recur(vector<string> &result, unordered_map<char, int> &count, string &curr, int len)
	    {
	        if (curr.size() == len)
	        {
	            result.push_back(curr);
	            return;
	        }
	        
	        for (auto iter = count.begin(); iter != count.end(); ++iter)
	        {
	            if (iter->second == 0) continue;
	            curr.push_back(iter->first);
	            --iter->second;
	            recur(result, count, curr, len);
	            ++iter->second;
	            curr.pop_back();
	        }
	    }
	    
	};