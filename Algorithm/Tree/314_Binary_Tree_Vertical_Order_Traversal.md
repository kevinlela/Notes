### Binary Tree Vertical Order Traversal
Given a binary tree, return the vertical order traversal of its nodes' values. (ie, from top to bottom, column by column).

If two nodes are in the same row and column, the order should be from left to right.

Examples:

Given binary tree [3,9,20,null,null,15,7],
   3
  /\
 /  \
 9  20
    /\
   /  \
  15   7
return its vertical order traversal as:
[
  [9],
  [3,15],
  [20],
  [7]
]
Given binary tree [3,9,8,4,0,1,7],
     3
    /\
   /  \
   9   8
  /\  /\
 /  \/  \
 4  01   7
return its vertical order traversal as:
[
  [4],
  [9],
  [3,0,1],
  [8],
  [7]
]
Given binary tree [3,9,8,4,0,1,7,null,null,null,2,5] (0's right child is 2 and 1's left child is 5),
     3
    /\
   /  \
   9   8
  /\  /\
 /  \/  \
 4  01   7
    /\
   /  \
   5   2
return its vertical order traversal as:
[
  [4],
  [9,5],
  [3,0,1],
  [8,2],
  [7]
]

[leetcode](https://leetcode.com/problems/binary-tree-vertical-order-traversal/description/)

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
	    vector<vector<int>> verticalOrder(TreeNode* root) {
	        // we need to know the index
	        // we can use hashmap
	        if (root == NULL) return vector<vector<int>> ();
	        unordered_map<int, vector<int>> resMap;
	        queue<pair<int, TreeNode*>> q;
	        q.push({0, root});
	        while (!q.empty())
	        {
	            int len = q.size();
	            for (int i = 0; i < len; ++i)
	            {
	                pair<int, TreeNode*> &p = q.front();
	                resMap[p.first].push_back(p.second->val);
	                if (p.second->left) q.push({p.first-1, p.second->left});
	                if (p.second->right) q.push({p.first+1, p.second->right});
	                q.pop();
	            }
	        }
	        
	        int minCol = INT_MAX, maxCol = INT_MIN;
	        for (auto it = resMap.begin(); it != resMap.end(); ++it)
	        {
	            minCol = min(minCol, it->first);
	            maxCol = max(maxCol, it->first);
	        }
	        
	        vector<vector<int>> result(maxCol - minCol + 1, vector<int>());
	        for (auto it = resMap.begin(); it != resMap.end(); ++it)
	        {
	            result[it->first - minCol] = it->second;
	        }
	        
	        return result;
	    }
	};
