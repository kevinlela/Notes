### Ransom Note
Given an arbitrary ransom note string and another string containing letters from all the magazines, write a function that will return true if the ransom note can be constructed from the magazines ; otherwise, it will return false.

Each letter in the magazine string can only be used once in your ransom note.

Note:
You may assume that both strings contain only lowercase letters.

canConstruct("a", "b") -> false
canConstruct("aa", "ab") -> false
canConstruct("aa", "aab") -> true

[leetcode](https://leetcode.com/problems/ransom-note/description/)

### Answer 

	class Solution {
	public:
	    bool canConstruct(string ransomNote, string magazine) {
	        //unordered_map<char, int> mcount;
	        vector<int> mcount(26, 0);
	        for (int i = 0; i < magazine.size(); ++i)
	        {
	            ++mcount[magazine[i] - 'a'];
	        }
	        
	        for (int i = 0; i < ransomNote.size(); ++i)
	        {
	            //if (mcount.find(ransomNote[i]) == mcount.end()) return false;
	            //else 
	            if (mcount[ransomNote[i] - 'a'] == 0) return false;
	            else --mcount[ransomNote[i] - 'a'];
	        }
	        
	        return true;
	    }
	};