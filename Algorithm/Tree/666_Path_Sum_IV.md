### Path Sum IV
If the depth of a tree is smaller than 5, then this tree can be represented by a list of three-digits integers.

For each integer in this list:
The hundreds digit represents the depth D of this node, 1 <= D <= 4.
The tens digit represents the position P of this node in the level it belongs to, 1 <= P <= 8. The position is the same as that in a full binary tree.
The units digit represents the value V of this node, 0 <= V <= 9.
Given a list of ascending three-digits integers representing a binary with the depth smaller than 5. You need to return the sum of all paths from the root towards the leaves.

Example 1:
Input: [113, 215, 221]
Output: 12
Explanation: 
The tree that the list represents is:
 
	    3
	   / \
	  5   1

The path sum is (3 + 5) + (3 + 1) = 12.
Example 2:
Input: [113, 221]
Output: 4
Explanation: 
The tree that the list represents is: 
	    
	    3
	     \
	      1

The path sum is (3 + 1) = 4.

[leetcode](https://leetcode.com/problems/path-sum-iv/description/)

### Answer
	class Solution {
	public:
	    int pathSum(vector<int>& nums) {
	        int len = nums.size();
	        if (len == 0) return 0;
	        vector<int> count(8, 0);
	        vector<int> tmp(8, 0);
	        int level = 4, lr = 8, result = 0;
	        for (int i = len - 1; i >= 0;)
	        {
	            if (nums[i]/100 < level)
	            {
	                --level;
	                lr /= 2;
	                for (int j = 0; j < lr; ++j)
	                {
	                    count[j] = tmp[j];
	                    tmp[j] = 0;
	                }
	            }
	            else
	            {
	                int idx = nums[i] % 100;
	                int val = idx % 10;
	                idx = idx / 10 - 1;
	                result += max(count[idx], 1)*val;
	                tmp[idx/2] += max(count[idx], 1);
	                --i;
	            }
	        }
	        
	        return result;
	        
	    }
	};