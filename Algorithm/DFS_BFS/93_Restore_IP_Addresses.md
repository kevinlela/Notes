### Restore IP Addresses
Given a string containing only digits, restore it by returning all possible valid IP address combinations.

For example:
Given "25525511135",

return ["255.255.11.135", "255.255.111.35"]. (Order does not matter)

[leetcode](https://leetcode.com/problems/restore-ip-addresses/description/)

### Answer 
Just need to notice we cannot have 0 prefix number like "01". The number of sections of an IP address is 4.

	class Solution {
	public:
	    vector<string> restoreIpAddresses(string s) {
	        vector<string> result;
	        string comb;
	        recur(result, comb, s, 4, 0);
	        return result;
	    }
	    
	    void recur(vector<string> &result, string &comb, const string &s, int fNum, int curr)
	    {
	        int len = s.size();
	        if (fNum == 0 && curr >= len)
	        {
	            comb.pop_back();
	            result.push_back(comb);
	            return;
	        }
	        
	        if (len - curr < fNum) return; 
	        if (len - curr > 3*fNum) return;
	        
	        int cLen = comb.size();
	        
	        int sRange = s[curr] == '0' ? curr + 1 : curr + 3;
	        string currSub;
	        for (; curr < sRange && curr < len; ++curr)
	        {
	            currSub += s[curr];
	            if (currSub.size() == 3 && currSub > "255") continue;
	            recur (result, comb + currSub + ".", s, fNum - 1, curr + 1);
	        }
	        
	        comb.erase(max(0, cLen - 1));
	    }
	};
