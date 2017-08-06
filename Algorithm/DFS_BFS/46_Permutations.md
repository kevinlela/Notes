### Permutations
Given a collection of distinct numbers, return all possible permutations.

For example,
[1,2,3] have the following permutations:
[
  [1,2,3],
  [1,3,2],
  [2,1,3],
  [2,3,1],
  [3,1,2],
  [3,2,1]
]

[leetcode](https://leetcode.com/problems/permutations/description/)

### Answer 
taditional backtracking problem

class Solution {
public:
    vector<vector<int>> permute(vector<int>& nums) {
        vector<vector<int>> result;
        recur(result, nums, 0);
        return result;
    }
    
    void recur(vector<vector<int>> &result, vector<int> &nums, int st)
    {
        if (st >= nums.size())
        {
            result.push_back(nums);
            return;
        }
        
        for (int i = st; i < nums.size(); ++i)
        {
            swap(nums[st], nums[i]);
            recur(result, nums, st + 1);
            swap(nums[st], nums[i]);
        }
    }
};