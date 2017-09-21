### Shortest Word Distance II
This is a follow up of Shortest Word Distance. The only difference is now you are given the list of words and your method will be called repeatedly many times with different parameters. How would you optimize it?

Design a class which receives a list of words in the constructor, and implements a method that takes two words word1 and word2 and return the shortest distance between these two words in the list.

For example,
Assume that words = ["practice", "makes", "perfect", "coding", "makes"].

Given word1 = “coding”, word2 = “practice”, return 3.
Given word1 = "makes", word2 = "coding", return 1.

Note:
You may assume that word1 does not equal to word2, and word1 and word2 are both in the list.

[leetcode](https://leetcode.com/problems/shortest-word-distance-ii/description/)

### Answer
It is a hash map + binary search problem
	class WordDistance {
	public:
	    WordDistance(vector<string> words) {
	        for (int i = 0; i < words.size(); ++i)
	        {
	            idx[words[i]].push_back(i);
	        }
	    }
	    
	    int shortest(string word1, string word2) {
	        vector<int> &idx1 = idx[word1];
	        vector<int> &idx2 = idx[word2];
	        return findShortest(idx1, idx2);
	    }
	private:
	    unordered_map<string, vector<int>> idx;
	    
	    int findShortest(const vector<int> &idx1, const vector<int> &idx2)
	    {
	        if (idx1.size() > idx2.size()) return findShortest(idx2, idx1);
	        int result = INT_MAX;
	        for (int i = 0; i < idx1.size(); ++i)
	        {
	            auto it = lower_bound(idx2.begin(), idx2.end(), idx1[i]);
	            if (it != idx2.end()) result = min(result, abs(*it - idx1[i]));
	            if (it != idx2.begin()) result = min(result, abs(*(it-1) - idx1[i]));
	        }
	        return result;
	    }
	};

	/**
	 * Your WordDistance object will be instantiated and called as such:
	 * WordDistance obj = new WordDistance(words);
	 * int param_1 = obj.shortest(word1,word2);
	 */