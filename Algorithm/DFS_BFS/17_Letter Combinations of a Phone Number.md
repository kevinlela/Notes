### Letter Combinations of a Phone Number

Given a digit string, return all possible letter combinations that the number could represent.

A mapping of digit to letters (just like on the telephone buttons) is given below.

Input:Digit string "23"
Output: ["ad", "ae", "af", "bd", "be", "bf", "cd", "ce", "cf"].
Note:
Although the above answer is in lexicographical order, your answer could be in any order you want.

[leetcode](https://leetcode.com/problems/letter-combinations-of-a-phone-number/description/)

### Answer:
It is a DFS problem

	class Solution {
	public:
	    vector<string> letterCombinations(string digits) {
	        vector<string> numMap = {"abc", "def", "ghi", "jkl", "mno", "pqrs", "tuv", "wxyz"};
	        vector<string> resultSet;
	        string result;
	        generateComb(resultSet, result, 0, digits, numMap);
	        return resultSet;
	    }
	    
	    void generateComb(vector<string> &resultSet, string &result, int st, 
	                      const string &digits, const vector<string> &numMap)
	    {
	        if (st >= digits.size())
	        {
	            if (!result.empty()) resultSet.push_back(result);
	            return;
	        }
	        
	        if (digits[st] < '2' || digits[st] > '9') generateComb(resultSet, result, st + 1, digits, numMap);
	        
	        int index = digits[st] - '2';
	        for (int i = 0; i < numMap[index].size(); ++i)
	        {
	            result.push_back(numMap[index][i]);
	            generateComb(resultSet, result, st + 1, digits, numMap);
	            result.pop_back();
	        }
	    }
	};