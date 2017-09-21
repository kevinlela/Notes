###  Closest Binary Search Tree Value II
Given a non-empty binary search tree and a target value, find k values in the BST that are closest to the target.

Note:
Given target value is a floating point.
You may assume k is always valid, that is: k ≤ total nodes.
You are guaranteed to have only one unique set of k values in the BST that are closest to the target.
Follow up:
Assume that the BST is balanced, could you solve it in less than O(n) runtime (where n = total nodes)?

[leetcode](https://leetcode.com/problems/closest-binary-search-tree-value-ii/description/)

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
	    vector<int> closestKValues(TreeNode* root, double target, int k) {
	        list<pair<double, int>> neg, pos;
	        stack<TreeNode*> stk;
	        while (root || !stk.empty())
	        {
	            if (root)
	            {
	                stk.push(root);
	                root = root->left;
	            }
	            else
	            {
	                double curr = stk.top()->val;
	                double diff = curr - target;
	                if (diff < 0)
	                {
	                    neg.push_front({abs(diff), curr});
	                    if (neg.size() > k) neg.pop_back();
	                }
	                else
	                {
	                    int len = neg.size() + pos.size();
	                    if (len == k)
	                    {
	                        if (neg.size() == 0) break;
	                        else if (diff > neg.rbegin()->first) break;
	                        else neg.pop_back(); 
	                    }
	                    pos.push_back({diff, curr});
	                }
	                root = stk.top()->right;
	                stk.pop();
	            }
	        }
	        
	        vector<int> result;
	        auto itNeg = neg.begin(), itPos = pos.begin();
	        while (itNeg != neg.end() || itPos != pos.end())
	        {
	            if (itNeg == neg.end()) result.push_back((itPos++)->second);
	            else if (itPos == pos.end()) result.push_back((itNeg++)->second);
	            else if (*itNeg < *itPos) result.push_back((itNeg++)->second);
	            else result.push_back((itPos++)->second);
	        }
	        
	        return result;
	    }
	};