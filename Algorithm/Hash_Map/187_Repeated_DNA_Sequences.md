### Repeated DNA Sequences
All DNA is composed of a series of nucleotides abbreviated as A, C, G, and T, for example: "ACGAATTCCG". When studying DNA, it is sometimes useful to identify repeated sequences within the DNA.

Write a function to find all the 10-letter-long sequences (substrings) that occur more than once in a DNA molecule.

For example,

Given s = "AAAAACCCCCAAAAACCCCCCAAAAAGGGTTT",

Return:
["AAAAACCCCC", "CCCCCAAAAA"].

[leetcode](https://leetcode.com/problems/repeated-dna-sequences/description/)

### Answer 
Could encode into number to speed up. 

	class Solution {
	public:
	    vector<string> findRepeatedDnaSequences(string s) {
	        unordered_map<string, int> counts;
	        int len = s.size();
	        
	        for (int k = 0; k < len - 9; ++k)
	        {
	            ++counts[s.substr(k, 10)];
	        }
	        
	        vector<string> result;
	        
	        for (auto iter = counts.begin(); iter != counts.end(); ++iter)
	        {
	            if (iter->second > 1) result.push_back(iter->first);
	        }
	        
	        return result;
	    }
	};