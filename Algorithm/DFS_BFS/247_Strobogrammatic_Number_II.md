### Strobogrammatic Number II
A strobogrammatic number is a number that looks the same when rotated 180 degrees (looked at upside down).

Find all strobogrammatic numbers that are of length = n.

For example,
Given n = 2, return ["11","69","88","96"].

[leetcode](https://leetcode.com/problems/strobogrammatic-number-ii/description/)

### Answer
We need consider several corner case
* if odd length, the center char cannot be 6 or 9
* the first letter cannot be 0 unless it is length 1

a better solution is to generate n/2 half, and manually generate the center. 

	class Solution {
	public:
	    vector<string> findStrobogrammatic(int n) {
	        // when you decide the first half, the second half is self decided
	        unordered_map<char, char> mapping = {{'0', '0'}, {'1', '1'}, {'6', '9'}, {'8', '8'}, {'9', '6'}};
	        vector<string> result;
	        string curr;
	        bool odd = n%2;
	        recur(result, curr, mapping, (n+1)/2, odd);
	        for (int i = 0; i < result.size(); ++i)
	        {
	            generateHalf(result[i], odd, mapping);
	        }
	        return result;
	    }
	    
	    void generateHalf(string &in, bool odd, const unordered_map<char, char> &mapping)
	    {
	        int len = in.size();
	        int st = odd ? (len - 2) : (len - 1);
	        for (st; st >= 0; --st)
	        {
	            auto it = mapping.find(in[st]);
	            in.push_back(it->second);
	        }
	    }
	    
	    void recur(vector<string> &result, string &curr, const unordered_map<char, char> &mapping, int n, bool odd)
	    {
	        if (curr.size() == n)
	        {
	            result.push_back(curr);
	            return;
	        }
	        
	        for (auto iter = mapping.cbegin(); iter != mapping.cend(); ++iter)
	        {
	            if (curr.size() == 0 && (n != 1 || !odd) && iter->first == '0') continue;
	            if (odd && curr.size() + 1 == n)
	            {
	                if (iter->first == '6' || iter->first == '9') continue;
	            }
	            curr.append(1, iter->first);
	            recur(result, curr, mapping, n, odd);
	            curr.pop_back();
	        }
	    }
	};