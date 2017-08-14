### House Robber III
The thief has found himself a new place for his thievery again. There is only one entrance to this area, called the "root." Besides the root, each house has one and only one parent house. After a tour, the smart thief realized that "all houses in this place forms a binary tree". It will automatically contact the police if two directly-linked houses were broken into on the same night.

Determine the maximum amount of money the thief can rob tonight without alerting the police.

Example 1:
     3
    / \
   2   3
    \   \ 
     3   1
Maximum amount of money the thief can rob = 3 + 3 + 1 = 7.
Example 2:
     3
    / \
   4   5
  / \   \ 
 1   3   1
Maximum amount of money the thief can rob = 4 + 5 = 9.

[leetcode](https://leetcode.com/problems/house-robber-iii/description/)

### Answer 
every node has two possibility
* steal + child's not steal
* not steal = max(l + r, l + r not steal, l not steal + r, l not steal + r not steal)

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
	    int rob(TreeNode* root) {
	        vector<int> result = recur(root);
	        return max(result[0], result[1]);
	    }
	    
	    vector<int> recur(TreeNode* iter)
	    {
	        if (iter == NULL) return vector<int> (2, 0);
	        vector<int> l_res = recur(iter->left);
	        vector<int> r_res = recur(iter->right);
	        
	        vector<int> res(2, 0);
	        // if steal, left right must all be not steal
	        res[0] = l_res[1] + r_res[1] + iter->val;
	        // if not steal
	        res[1] = l_res[0] + r_res[0];
	        res[1] = max(res[1], l_res[1] + r_res[1]);
	        res[1] = max(res[1], l_res[0] + r_res[1]);
	        res[1] = max(res[1], l_res[1] + r_res[0]);
	        
	        return res;
	    }
	};