### Most Frequent Subtree Sum
Given the root of a tree, you are asked to find the most frequent subtree sum. The subtree sum of a node is defined as the sum of all the node values formed by the subtree rooted at that node (including the node itself). So what is the most frequent subtree sum value? If there is a tie, return all the values with the highest frequency in any order.

Examples 1
Input:

  5
 /  \
2   -3
return [2, -3, 4], since all the values happen only once, return all of them in any order.
Examples 2
Input:

  5
 /  \
2   -5
return [2], since 2 happens twice, however -5 only occur once.
Note: You may assume the sum of values in any subtree is in the range of 32-bit signed integer.

[leetcode](https://leetcode.com/problems/most-frequent-subtree-sum/description/)

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
	    unordered_map<int, int> counts;
	    vector<int> findFrequentTreeSum(TreeNode* root) {
	        vector<int> result;
	        int maxCount = 0;
	        recur(root, result, maxCount);
	        return result;
	    }
	    
	    int recur(TreeNode* iter, vector<int> &result, int &maxCount)
	    {
	        if (iter == NULL) return 0;
	        int left = recur(iter->left, result, maxCount);
	        int right = recur(iter->right, result, maxCount);
	        int sum = left + right + iter->val;
	        ++counts[sum];
	        if (counts[sum] == maxCount) result.push_back(sum);
	        else if (counts[sum] > maxCount)
	        {
	            result.clear();
	            result.push_back(sum);
	            maxCount = counts[sum];
	        }
	        return sum;
	    }
	};