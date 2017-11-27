### Construct Binary Tree from String
You need to construct a binary tree from a string consisting of parenthesis and integers.

The whole input represents a binary tree. It contains an integer followed by zero, one or two pairs of parenthesis. The integer represents the root's value and a pair of parenthesis contains a child binary tree with the same structure.

You always start to construct the left child node of the parent first if it exists.

Example:
Input: "4(2(3)(1))(6(5))"
Output: return the tree root node representing the following tree:

	       4
	     /   \
	    2     6
	   / \   / 
	  3   1 5   
Note:
There will only be '(', ')', '-' and '0' ~ '9' in the input string.
An empty tree is represented by "" instead of "()".

[leetcode](https://leetcode.com/problems/construct-binary-tree-from-string/description/)

### Answer
	/**
	 * Definition for a binary tree node.
	 * struct TreeNode {
	 *     int val;
	 *     TreeNode *left;
	 *     TreeNode *right;
	 *     TreeNode(int x) : val(x), left(NULL), right(NULL) {}
	 * };
	 */
	class Solution {
	public:
	    TreeNode* str2tree(string s) {
	        string curr = "";
	        stack<TreeNode*> stk;
	        
	        int i = 0; 
	        for (i = 0; i < s.size(); ++i)
	        {
	            if (s[i] == '(') break;
	            curr.append(1, s[i]);
	        }
	        if (curr.empty()) return NULL;
	        
	        stk.push( new TreeNode ( atoi(curr.c_str()) ) );
	        
	        curr = "";
	        
	        for (i; i < s.size(); )
	        {
	            if (s[i] == '(')
	            {
	                ++i;
	                curr = "";
	                for (i; i < s.size(); ++i)
	                {
	                    if (s[i] == '(' || s[i] == ')') break;
	                    curr.append(1, s[i]);
	                }
	                
	                TreeNode *n = new TreeNode (atoi(curr.c_str()));
	                //cout << n->val << endl;
	                if (!stk.empty())
	                {
	                    if (stk.top()->left) stk.top()->right = n;
	                    else stk.top()->left = n;
	                }
	                stk.push(n);
	            }
	            else if (s[i] == ')')
	            {
	                stk.pop();
	                ++i;
	            }
	        }
	        
	        if (stk.empty()) return NULL;
	        return stk.top();
	    }
	};