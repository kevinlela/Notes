### 132 Pattern *
Given a sequence of n integers a1, a2, ..., an, a 132 pattern is a subsequence ai, aj, ak such that i < j < k and ai < ak < aj. Design an algorithm that takes a list of n numbers as input and checks whether there is a 132 pattern in the list.

Note: n will be less than 15,000.

Example 1:
Input: [1, 2, 3, 4]

Output: False

Explanation: There is no 132 pattern in the sequence.
Example 2:
Input: [3, 1, 4, 2]

Output: True

Explanation: There is a 132 pattern in the sequence: [1, 4, 2].
Example 3:
Input: [-1, 3, 2, 0]

Output: True

Explanation: There are three 132 patterns in the sequence: [-1, 3, 2], [-1, 3, 0] and [-1, 2, 0].

[leetcode](https://leetcode.com/problems/132-pattern/description/)

### Answer
we want a_k as larget as possible and a_j also as large as possible
In the other way, given a a[i], we want to find the optimal a_k and a_j
maintain a_k to be large element and stack of a_j to be all possible. 

for an a_k we have two possibility
1) a_i < a_k: job done

2) a_i > a_k: 
	* a_i < a_j: old a_j can be new a_k (since a_j > a_k) and a_i becomes new a_j
	* a_i > a_j: just add a_i to be the candidate of a_j

3) a_k == a_j: this means nothing

Why we need to traverse from back? because we can maintain a_k and a_j together, otherwise if we maintain a_i and a_j, that makes algorithm impossible. because even if ai < aj, we need both of them to compare to a_k

	class Solution {
	public:
	    bool find132pattern(vector<int>& nums) {
	        int len = nums.size();
	        if (len < 3) return false;
	        
	        int s3 = INT_MIN;
	        stack<int> myStk;
	        for (int i = len - 1; i >= 0; --i)
	        {
	            if (nums[i] < s3) return true;
	            else
	            {
	                while (!myStk.empty() && myStk.top() < nums[i])
	                {
	                    s3 = myStk.top();
	                    myStk.pop();
	                }
	                myStk.push(nums[i]);
	            }
	        }
	        return false;
	    }
	};
