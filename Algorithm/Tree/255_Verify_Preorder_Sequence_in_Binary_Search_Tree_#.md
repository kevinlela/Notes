### Verify Preorder Sequence in Binary Search Tree
Given an array of numbers, verify whether it is the correct preorder traversal sequence of a binary search tree.

You may assume each number in the sequence is unique.

Follow up:
Could you do it using only constant space complexity?

[leetcode](https://leetcode.com/problems/verify-preorder-sequence-in-binary-search-tree/description/)

### Answer
To me this problem is hard

1. preorder keeps decrease when iterate to left
2. when it goes up, it means comes to the right tree
3. all the value in the right tree must be larger than the last node

class Solution {
public:
    bool verifyPreorder(vector<int>& preorder) {
        stack<int> stk;
        int thre = INT_MIN; 
        for (int i = 0; i < preorder.size(); ++i)
        {
            if (stk.empty() || preorder[i] < stk.top())
            {
                if (preorder[i] < thre) return false;
                stk.push(preorder[i]);
            }
            else 
            {
                thre = stk.top();
                stk.pop();
                --i;
            }
        }
        
        return true;
    }
};






