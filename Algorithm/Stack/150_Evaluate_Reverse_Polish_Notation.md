### Evaluate Reverse Polish Notation
Evaluate the value of an arithmetic expression in Reverse Polish Notation.

Valid operators are +, -, \*, /. Each operand may be an integer or another expression.

Some examples:
  ["2", "1", "+", "3", "\*"] -> ((2 + 1) * 3) -> 9
  ["4", "13", "5", "/", "+"] -> (4 + (13 / 5)) -> 6

[leetcode](https://leetcode.com/problems/evaluate-reverse-polish-notation/description/)

### Answer 

	class Solution {
	public:
	    int evalRPN(vector<string>& tokens) {
	        stack<int> stk;
	        for (int k = 0; k < tokens.size(); k++)
	        {
	            if      (tokens[k] == "+") stk.push(opTwoNum(0, stk));
	            else if (tokens[k] == "-") stk.push(opTwoNum(1, stk));
	            else if (tokens[k] == "*") stk.push(opTwoNum(2, stk));
	            else if (tokens[k] == "/") stk.push(opTwoNum(3, stk));
	            else stk.push(stoi(tokens[k]));
	        }
	        
	        return stk.empty() ? 0 : stk.top();
	    }
	    
	    int opTwoNum(int op, stack<int> &stk)
	    {
	        int b = stk.top();
	        stk.pop();
	        int a = stk.top();
	        stk.pop();
	        if (op == 0) return a + b;
	        else if (op == 1) return a - b;
	        else if (op == 2) return a * b;
	        return a / b;
	    }
	};