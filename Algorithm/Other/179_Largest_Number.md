### Largest Number
Given a list of non negative integers, arrange them such that they form the largest number.

For example, given [3, 30, 34, 5, 9], the largest formed number is 9534330.

Note: The result may be very large, so you need to return a string instead of an integer.

[leetcode](https://leetcode.com/problems/largest-number/description/)

### Answer 
This is a very tricky problem, the largest number actually formed by lex order. 

	class Solution {
	public:
	    struct strCombCmp{
	        bool operator ()(const string& a, const string &b)
	        {
	            return a + b > b + a;
	        }
	    };
	    
	    string largestNumber(vector<int>& nums) {
	        string result;
	        if (nums.size() == 0) return result;
	        
	        vector<string> numStrs;
	        for (int k = 0; k < nums.size(); ++k)
	        {
	            numStrs.push_back(to_string(nums[k]));
	        }
	        
	        sort(numStrs.begin(), numStrs.end(), strCombCmp());
	        
	        for (int k = 0; k < numStrs.size(); ++k)
	        {
	            result += numStrs[k];
	        }
	        
	        int initNonZero = 0, resLen = result.size();
	        for (; initNonZero < resLen; ++initNonZero)
	        {
	            if (result[initNonZero] != '0') break;
	        }
	        
	        return result.substr(min(resLen - 1, initNonZero));
	    }
	};