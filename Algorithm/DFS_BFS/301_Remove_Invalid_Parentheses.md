### Remove Invalid Parentheses
Remove the minimum number of invalid parentheses in order to make the input string valid. Return all possible results.

Note: The input string may contain letters other than the parentheses ( and ).

Examples:
"()())()" -> ["()()()", "(())()"]
"(a)())()" -> ["(a)()()", "(a())()"]
")(" -> [""]

[leetcode](https://leetcode.com/problems/remove-invalid-parentheses/description/)

### Answer 
* count how many left and right is invalid
* use current left to track valid status
* use left and right to determine how many of them need to be removed

	class Solution {
	public:
	    vector<string> removeInvalidParentheses(string s) {
	        // left and right represent how many left and right needs to be removed
	        int left = 0, right = 0;
	        for (int i = 0; i < s.size(); ++i)
	        {
	            if (s[i] == '(') ++left;
	            if (s[i] == ')')
	            {
	                if (left > 0) --left;
	                else ++right;
	            }
	        }
	        unordered_set<string> result;
	        recur(result, 0, s, "", left, right, 0);
	        
	        vector<string> res;
	        for (auto iter = result.begin(); iter != result.end(); ++iter)
	        {
	            res.push_back(*iter);
	        }
	        return res;
	    }
	    
	    void recur(unordered_set<string> &result, int left,
	               const string &s, string curr, 
	               int left_remain, int right_remain, int currIdx)
	    {
	        if (left == 0 && 
	            left_remain == 0 && right_remain == 0 && 
	            currIdx >= s.size())
	        {
	            result.insert(curr);
	            return;
	        }
	        if (currIdx >= s.size()) return;
	        
	        if (s[currIdx] != '(' && s[currIdx] != ')')
	        {
	            recur(result, left, s, curr + s[currIdx], 
	                  left_remain, right_remain, currIdx + 1);
	        }
	        else if (s[currIdx] == '(')
	        {
	            if (left_remain > 0)
	            {
	                recur(result, left, s, curr, left_remain - 1, right_remain, 
	                      currIdx + 1);
	            }
	            recur(result, left + 1, s, curr + s[currIdx], left_remain, 
	                  right_remain, currIdx + 1);
	        }
	        else
	        {
	            if (right_remain > 0)
	            {
	                recur(result, left, s, curr, left_remain, right_remain - 1, 
	                      currIdx + 1);
	            }
	            if (left > 0)
	            {
	                recur(result, left - 1, s, curr + s[currIdx], left_remain,
	                      right_remain, currIdx + 1);
	            }
	        }
	    }
	};