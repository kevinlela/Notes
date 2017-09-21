### Unique Word Abbreviation
An abbreviation of a word follows the form <first letter><number><last letter>. Below are some examples of word abbreviations:

a) it                      --> it    (no abbreviation)

     1
b) d|o|g                   --> d1g

              1    1  1
     1---5----0----5--8
c) i|nternationalizatio|n  --> i18n

              1
     1---5----0
d) l|ocalizatio|n          --> l10n
Assume you have a dictionary and given a word, find whether its abbreviation is unique in the dictionary. A word's abbreviation is unique if no other word from the dictionary has the same abbreviation.

Example: 
Given dictionary = [ "deer", "door", "cake", "card" ]

isUnique("dear") -> 
false

isUnique("cart") -> 
true

isUnique("cane") -> 
false

isUnique("make") -> 
true

[leetcode](https://leetcode.com/problems/unique-word-abbreviation/description/)

### Answer
The only difficulty here is the dictionary itself, some word may not be unique and also the input word may exist in the initialization vector. 

	class ValidWordAbbr {
	public:
	    ValidWordAbbr(vector<string> dictionary) {
	        for (int i = 0; i < dictionary.size(); ++i)
	        {
	            d_full.insert(dictionary[i]);
	        }
	        
	        for (auto it = d_full.begin(); it != d_full.end(); ++it)
	        {
	            ++d_dict[genAbbr(*it)];
	        }
	    }
	    
	    bool isUnique(string word) {
	        string wAbbr = genAbbr(word);
	        if (d_full.find(word) == d_full.end())
	        {
	            if (d_dict.find(wAbbr) == d_dict.end()) return true;
	            else return false;
	        }
	        else // the word alreay existing in the dict
	        {
	            if (d_dict[wAbbr] == 1) return true;
	            else return false;
	        }
	        return false;
	    }
	    
	private:
	    string genAbbr(const string &s)
	    {
	        if (s.size() < 2) return s;
	        int len = s.size();
	        string result = "";
	        result.append(1, s[0]);
	        result += to_string(len - 2);
	        result.append(1, s[len-1]);
	        return result;
	    }
	    
	    unordered_map<string, int> d_dict;
	    unordered_set<string> d_full;
	    
	};

	/**
	 * Your ValidWordAbbr object will be instantiated and called as such:
	 * ValidWordAbbr obj = new ValidWordAbbr(dictionary);
	 * bool param_1 = obj.isUnique(word);
	 */