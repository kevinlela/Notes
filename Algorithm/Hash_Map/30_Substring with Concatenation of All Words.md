### Substring with Concatenation of All Words

You are given a string, s, and a list of words, words, that are all of the same length. Find all starting indices of substring(s) in s that is a concatenation of each word in words exactly once and without any intervening characters.

For example, given:
s: "barfoothefoobarman"
words: ["foo", "bar"]

You should return the indices: [0,9].
(order does not matter).

[leetcode]{https://leetcode.com/problems/substring-with-concatenation-of-all-words/description/}

### Answer:

I use quite a brutal force way to solve this problem. However, actually, we just need wordLen starting point and use a two pointer window approach (revisit)

	class Solution {
	public:
	    vector<int> findSubstring(string s, vector<string>& words) {
	        vector<int> result;
	        if (s.length() == 0 || words.size() == 0) return result;
	        int sLen = s.length();
	        int wLen = words[0].length(); // words are in the same length
	        int subLen = wLen * words.size(); // words for all concatenated string
	        
	        unordered_map<string, int> allWords;
	        for (int i = 0; i < words.size(); ++i)
	        {
	            allWords[words[i]]++;
	        }
	        
	        for (int i = 0; i <= sLen - subLen; ++i)
	        {
	            unordered_map<string, int> tmp = allWords;
	            int j = 0;
	            for (; j < words.size(); ++j)
	            {
	                string curr = s.substr(i + j*wLen, wLen);
	                if (tmp.find(curr) == tmp.end()) break;
	                else if (tmp[curr] == 0) break;
	                else --tmp[curr];
	            }
	            if (j == words.size()) result.push_back(i);
	        }
	        
	        return result;
	    }
	};