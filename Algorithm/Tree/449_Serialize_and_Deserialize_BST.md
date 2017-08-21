### Serialize and Deserialize BST
Serialization is the process of converting a data structure or object into a sequence of bits so that it can be stored in a file or memory buffer, or transmitted across a network connection link to be reconstructed later in the same or another computer environment.

Design an algorithm to serialize and deserialize a binary search tree. There is no restriction on how your serialization/deserialization algorithm should work. You just need to ensure that a binary search tree can be serialized to a string and this string can be deserialized to the original tree structure.

The encoded string should be as compact as possible.

Note: Do not use class member/global/static variables to store states. Your serialize and deserialize algorithms should be stateless.

[leetcode](https://leetcode.com/problems/serialize-and-deserialize-bst/description/)

### Answer
We just need a flag to indicate NULL node. and use DFS to traverse the tree
	/**
	 * Definition for a binary tree node.
	 * struct TreeNode {
	 *     int val;
	 *     TreeNode *left;
	 *     TreeNode *right;
	 *     TreeNode(int x) : val(x), left(NULL), right(NULL) {}
	 * };
	 */
	class Codec {
	public:

	    // Encodes a tree to a single string.
	    string serialize(TreeNode* root) {
	        if (root == NULL) return "#";
	        return to_string(root->val) + "," + serialize(root->left) + "," + serialize(root->right);
	    }

	    // Decodes your encoded data to tree.
	    TreeNode* deserialize(string data) {
	        int iter = 0;
	        return decode(data, iter);
	    }
	    
	    TreeNode* decode(const string &data, int& iter)
	    {
	        if (iter >= data.size()) return NULL;
	        
	        string curr_str;
	        for (iter; iter < data.size(); ++iter)
	        {
	            if (data[iter] == ',') break;
	            curr_str.append(1, data[iter]);
	        }
	        ++iter;
	        
	        if (curr_str.size() == 1 && curr_str[0] == '#') return NULL;
	        
	        TreeNode *curr = new TreeNode (stoi(curr_str));
	        curr->left  = decode(data, iter);
	        curr->right = decode(data, iter);
	        
	        return curr;
	    }
	};

	// Your Codec object will be instantiated and called as such:
	// Codec codec;
	// codec.deserialize(codec.serialize(root));
