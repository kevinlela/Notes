### Binary Tree Longest Consecutive Sequence II
Given a binary tree, you need to find the length of Longest Consecutive Path in Binary Tree.

Especially, this path can be either increasing or decreasing. For example, [1,2,3,4] and [4,3,2,1] are both considered valid, but the path [1,2,4,3] is not valid. On the other hand, the path can be in the child-Parent-child order, where not necessarily be parent-child order.

Example 1:
Input:
        1
       / \
      2   3
Output: 2
Explanation: The longest consecutive path is [1, 2] or [2, 1].
Example 2:
Input:
        2
       / \
      1   3
Output: 3
Explanation: The longest consecutive path is [1, 2, 3] or [3, 2, 1].
Note: All the values of tree nodes are in the range of [-1e7, 1e7].


[leetcode](https://leetcode.com/problems/binary-tree-longest-consecutive-sequence-ii/description/)

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
	    int longestConsecutive(TreeNode* root) {
	        // every node has two status, decreasing or increasing, and count for each    
	        int result = 0;
	        recur(root, result);
	        return result;
	    }
	    
	    pair<int, int> recur(TreeNode* iter, int &result)
	    {
	        if (iter == NULL) return {0, 0};
	        int ld = 0, li = 0, rd = 0, ri = 0;
	        if (iter->left)
	        {
	            pair<int, int> l = recur(iter->left, result);
	            if (iter->left->val + 1 == iter->val) // increasing
	                li = l.first;
	            if (iter->left->val - 1 == iter->val) //decreasing
	                ld = l.second;
	        }
	        if (iter->right)
	        {
	            pair<int, int> r = recur(iter->right, result);
	            if (iter->right->val + 1 == iter->val) // increasing
	                ri = r.first;
	            if (iter->right->val - 1 == iter->val) //decreasing
	                rd = r.second;
	        }
	        
	        result = max(result, li + rd + 1);
	        result = max(result, ld + ri + 1);
	        
	        return {max(li, ri) + 1, max(ld, rd) + 1};   
	    }
	};