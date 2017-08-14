### Binary Tree Paths
Given a binary tree, return all root-to-leaf paths.

For example, given the following binary tree:

   1
 /   \
2     3
 \
  5
All root-to-leaf paths are:

["1->2->5", "1->3"]

[leetcode](https://leetcode.com/problems/binary-tree-paths/description/)

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
	    vector<string> binaryTreePaths(TreeNode* root) {
	        vector<string> result;
	        recur(root, "", result);
	        return result;
	    }
	    
	    void recur(TreeNode* iter, string path, vector<string> &result)
	    {
	        if (iter == NULL) return;
	        if (iter->left == NULL && iter->right == NULL)
	        {
	            path += to_string(iter->val);
	            result.push_back(path);
	            return;
	        }
	        
	        path += to_string(iter->val) + "->";
	        recur(iter->left, path, result);
	        recur(iter->right, path, result);
	    }
	};