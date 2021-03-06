### Verify Preorder Serialization of a Binary Tree
One way to serialize a binary tree is to use pre-order traversal. When we encounter a non-null node, we record the node's value. If it is a null node, we record using a sentinel value such as #.

     _9_
    /   \
   3     2
  / \   / \
 4   1  #  6
/ \ / \   / \
# # # #   # #
For example, the above binary tree can be serialized to the string "9,3,4,#,#,1,#,#,2,#,6,#,#", where # represents a null node.

Given a string of comma separated values, verify whether it is a correct preorder traversal serialization of a binary tree. Find an algorithm without reconstructing the tree.

Each comma separated value in the string must be either an integer or a character '#' representing null pointer.

You may assume that the input format is always valid, for example it could never contain two consecutive commas such as "1,,3".

Example 1:
"9,3,4,#,#,1,#,#,2,#,6,#,#"
Return true

Example 2:
"1,#"
Return false

Example 3:
"9,#,#,1"
Return false

[leetcode](https://leetcode.com/problems/verify-preorder-serialization-of-a-binary-tree/description/)

### Answer 
Delete node from the end, every node needs two '#' to compromise. 

	class Solution {
	public:
	    bool isValidSerialization(string preorder) {
	        int pounds = 0;
	        while (!preorder.empty())
	        {
	            char c = *(preorder.rbegin());
	            if (c == '#') 
	            {
	                ++pounds;
	                preorder.pop_back();
	            }
	            else if (c == ',') preorder.pop_back();
	            else
	            {
	                while (!preorder.empty() && *(preorder.rbegin()) != ',') preorder.pop_back();
	                pounds -= 2;
	                if (pounds < 0) return false;
	                ++pounds;
	            }
	        }
	        
	        return pounds == 1 || pounds == 0;
	    }
	};