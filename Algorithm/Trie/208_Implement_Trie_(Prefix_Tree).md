### Implement Trie (Prefix Tree)
Implement a trie with insert, search, and startsWith methods.

Note:
You may assume that all inputs are consist of lowercase letters a-z.

[leetcode](https://leetcode.com/problems/implement-trie-prefix-tree/description/)

### Answer 

	class Trie {
	public:
	    struct TrieNode {
	        char val;
	        unordered_map<char, TrieNode*> nei;
	        bool isWord;
	        TrieNode(char inVal) : val(inVal), isWord(false){}
	    };
	    
	    /** Initialize your data structure here. */
	    Trie() {
	        root = new TrieNode (0);
	    }
	    
	    /** Inserts a word into the trie. */
	    void insert(const string &word) {
	        int len = word.size(), k = 0;
	        TrieNode* pos = getPrefix(word, k);
	        for (int i = k; i < len; ++i)
	        {
	            unordered_map<char, TrieNode*> &nei = pos->nei;
	            nei[word[i]] = new TrieNode(word[i]);
	            pos = nei[word[i]];
	        }
	        pos->isWord = true;
	    }
	    
	    /** Returns if the word is in the trie. */
	    bool search(const string &word) {
	        int len = word.size(), k = 0;
	        TrieNode* pos = getPrefix(word, k);
	        return k == len && pos->isWord == true;
	    }
	    
	    /** Returns if there is any word in the trie that starts with the given prefix. */
	    bool startsWith(const string &prefix) {
	        int len = prefix.size(), k = 0;
	        getPrefix(prefix, k);
	        return k == len;
	    }
	    
	    TrieNode* getPrefix(const string &word, int &k)
	    {
	        TrieNode* iter = root;
	        int len = word.size();
	        for (k = 0; k < len; ++k)
	        {
	            unordered_map<char, TrieNode*> &nei = iter->nei;
	            if (nei.find(word[k]) == nei.end()) return iter;
	            iter = nei[word[k]];
	        }
	        return iter;
	    }
	private:
	    TrieNode *root;
	};

	/**
	 * Your Trie object will be instantiated and called as such:
	 * Trie obj = new Trie();
	 * obj.insert(word);
	 * bool param_2 = obj.search(word);
	 * bool param_3 = obj.startsWith(prefix);
	 */