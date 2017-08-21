### Sort Characters By Frequency
Given a string, sort it in decreasing order based on the frequency of characters.

Example 1:

Input:
"tree"

Output:
"eert"

Explanation:
'e' appears twice while 'r' and 't' both appear once.
So 'e' must appear before both 'r' and 't'. Therefore "eetr" is also a valid answer.
Example 2:

Input:
"cccaaa"

Output:
"cccaaa"

Explanation:
Both 'c' and 'a' appear three times, so "aaaccc" is also a valid answer.
Note that "cacaca" is incorrect, as the same characters must be together.
Example 3:

Input:
"Aabb"

Output:
"bbAa"

Explanation:
"bbaA" is also a valid answer, but "Aabb" is incorrect.
Note that 'A' and 'a' are treated as two different characters.

[leetcode](https://leetcode.com/problems/sort-characters-by-frequency/description/)

### Answer
It can also use Bucket sort to create freq array vector<int, vector<int>> with size s.size(). 

This worthy to note that the bucket sort gives result O(2N), my solution gives O(N) + O(min(N, # of different char)log min(N, # of different char)). For this problem, it is not necessary that my solution is worse.

	class Solution {
	public:
	    struct less_than{
	        inline bool operator() (const pair<char, int> &a, 
	                                const pair<char, int> &b)
	        {
	            return a.second > b.second;
	        }
	    };
	    
	    string frequencySort(string s) {
	        if (s.empty()) return "";
	        
	        unordered_map<char, int> countsMap;
	        
	        for (int i = 0; i < s.size(); ++i)
	        {
	            ++countsMap[s[i]];
	        }
	        
	        vector<pair<char, int>> counts;
	        for (auto iter = countsMap.begin(); iter != countsMap.end(); ++iter)
	        {
	            counts.push_back({iter->first, iter->second});
	        }
	        
	        sort(counts.begin(), counts.end(), less_than());
	        
	        string result;
	        
	        for (int i = 0; i < counts.size(); ++i)
	        {
	            result.append(counts[i].second, counts[i].first);
	        }
	        
	        return result;
	    }
	};
