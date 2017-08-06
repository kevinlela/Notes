### Binary Tree Level Order Traversal
Given a binary tree, return the level order traversal of its nodes' values. (ie, from left to right, level by level).

For example:
Given binary tree [3,9,20,null,null,15,7],
    3
   / \
  9  20
    /  \
   15   7
return its level order traversal as:
[
  [3],
  [9,20],
  [15,7]
]

[leetcode](https://leetcode.com/problems/binary-tree-level-order-traversal/description/)

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
    vector<vector<int>> levelOrder(TreeNode* root) {
        vector<vector<int>> result;
        if (root == NULL) return result;
        queue<TreeNode*> cands;
        cands.push(root);
        while (!cands.empty())
        {
            vector<int> level;
            int len = cands.size();
            for (int i = 0; i < len; ++i)
            {
                TreeNode* curr = cands.front();
                level.push_back(curr->val);
                if (curr->left) cands.push(curr->left);
                if (curr->right) cands.push(curr->right);
                cands.pop();
            }
            result.push_back(level);
        }
        return result;
    }
};