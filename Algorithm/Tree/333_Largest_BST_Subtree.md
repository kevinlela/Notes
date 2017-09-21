### Largest BST Subtree
Given a binary tree, find the largest subtree which is a Binary Search Tree (BST), where largest means subtree with largest number of nodes in it.

Note:
A subtree must include all of its descendants.
Here's an example:
    10
    / \
   5  15
  / \   \ 
 1   8   7
The Largest BST Subtree in this case is the highlighted one. 
The return value is the subtree's size, which is 3.
Follow up:
Can you figure out ways to solve it with O(n) time complexity?

[leetcode](https://leetcode.com/problems/largest-bst-subtree/description/)

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
	private:
	    class BstNode{
	    public:
	        BstNode(int left, int right, bool isBst, int num) 
	            : d_left(left), d_right(right), d_isBst(isBst), d_num(num){}
	        int d_left;
	        int d_right;
	        int d_isBst;
	        int d_num;
	    };
	    
	public:
	    int largestBSTSubtree(TreeNode* root) {
	        // to determine the bst, we need to return the interval of left and right childs
	        // at the same time, we need to return whether the lower subtree is bst or not
	        int result = 0;
	        recur(root, result);
	        return result;
	    }
	    
	    BstNode recur(TreeNode *iter, int &result)
	    {
	        if (iter == NULL) return BstNode(0, 0, true, 0); // only happend when root == NULL
	        BstNode curr(iter->val, iter->val, true, 1);
	        if (iter->left)
	        {
	            BstNode left = recur(iter->left, result);
	            if (!left.d_isBst || iter->val <= left.d_right) curr.d_isBst = false;
	            else
	            {
	                curr.d_left = left.d_left;
	               curr.d_num += left.d_num;
	            }
	        }
	        if (iter->right)
	        {
	            BstNode right = recur(iter->right, result);
	            if (!right.d_isBst || iter->val >= right.d_left) curr.d_isBst = false;
	            else
	            {
	                curr.d_right = right.d_right;
	                curr.d_num  += right.d_num;
	            }
	        }
	        if (curr.d_isBst) result = max(result, curr.d_num);
	        return curr;
	    }
	};