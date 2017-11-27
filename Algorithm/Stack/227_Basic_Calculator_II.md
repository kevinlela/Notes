
### Basic Calculator II
mplement a basic calculator to evaluate a simple expression string.

The expression string contains only non-negative integers, +, -, \*, / operators and empty spaces . The integer division should truncate toward zero.

You may assume that the given expression is always valid.

Some examples:
"3+2\*2" = 7
" 3/2 " = 1
" 3+5 / 2 " = 5
Note: Do not use the eval built-in library function.

[leetcode](https://leetcode.com/problems/basic-calculator-ii/description/)

### Answer 
use the stack to store all plus numbers. 

	class Solution {
	public:
	    int calculate(string s) {
	        char op = '+';
	        stack<int> myStk;
	        for (int i = 0; i < s.size(); ++i)
	        {
	            if (  s[i] == '+' || s[i] == '-'
	                ||s[i] == '*' || s[i] == '/' )
	            {
	                op = s[i];
	            }
	            else //it is number
	            {
	                int curr = getNextNum(s, i);
	                if (op == '+') myStk.push(curr);
	                else if (op == '-') myStk.push(-curr);
	                else if (op == '*') myStk.top() = myStk.top()*curr;
	                else myStk.top() = myStk.top()/curr;
	            }
	        }
	        
	        int len = myStk.size(), result = 0;
	        for (int i = 0; i < len; ++i)
	        {
	            result += myStk.top();
	            myStk.pop();
	        }
	        return result;
	    }
	    
	    int getNextNum(const string &s, int &i)
	    {
	        string num;
	        for (; i < s.size(); ++i)
	        {
	            if (isdigit(s[i])) num += s[i];
	            if (  s[i] == '+' || s[i] == '-'
	                ||s[i] == '*' || s[i] == '/' )
	            {
	                break;
	            }
	        }
	        
	        --i;
	        return stoi(num);
	    }
	    
	};