### Different Ways to Add Parentheses
Given a string of numbers and operators, return all possible results from computing all the different possible ways to group numbers and operators. The valid operators are +, - and *.


Example 1
Input: "2-1-1".

((2-1)-1) = 0
(2-(1-1)) = 2
Output: [0, 2]


Example 2
Input: "2*3-4*5"

(2*(3-(4*5))) = -34
((2*3)-(4*5)) = -14
((2*(3-4))*5) = -10
(2*((3-4)*5)) = -10
(((2*3)-4)*5) = 10
Output: [-34, -14, -10, -10, 10]

[leetcode](https://leetcode.com/problems/different-ways-to-add-parentheses/description/)

### Answer 

	class Solution {
	public:
	    vector<int> diffWaysToCompute(string input) {
	        vector<char> ops;
	        vector<int> nums;
	        
	        string numStr;
	        for (int i = 0; i < input.size(); ++i)
	        {
	            if(input[i] == '+' || input[i] == '-' || input[i] == '*')
	            {
	                ops.push_back(input[i]);
	                nums.push_back(stoi(numStr));
	                numStr.clear();
	            }
	            else numStr.append(1, input[i]);
	        }
	        nums.push_back(stoi(numStr));
	        
	        int len = nums.size();
	        
	        return recur(ops, nums, 0, len - 1);
	        
	    }
	    
	    vector<int> recur(const vector<char> &ops, const vector<int> &nums, int st, int ed)
	    {
	        if (st == ed) return vector<int> (1, nums[st]);
	        
	        vector<int> result;
	        for (int i = st; i <= ed - 1; ++i)
	        {
	            vector<int> left = recur(ops, nums, st, i);
	            vector<int> right = recur(ops, nums, i + 1, ed);
	            for (int n = 0; n < left.size(); ++n)
	            {
	                for (int m = 0; m < right.size(); ++m)
	                {
	                    result.push_back(op2num(left[n], right[m], ops[i]));
	                }
	            }
	        }
	        
	        return result;
	    }
	    
	    int op2num(int a, int b, char op)
	    {
	        if (op == '+') return a + b;
	        else if (op == '-') return a - b;
	        return a*b;
	    }
	};