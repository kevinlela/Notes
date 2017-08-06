### Permutation Sequence
The set [1,2,3,…,n] contains a total of n! unique permutations.

By listing and labeling all of the permutations in order,
We get the following sequence (ie, for n = 3):

"123"
"132"
"213"
"231"
"312"
"321"
Given n and k, return the kth permutation sequence.

Note: Given n will be between 1 and 9 inclusive.

[leetcode](https://leetcode.com/problems/permutation-sequence/description/)

### Answer 

the period for the first element is (n-1)! and the second is (n-2)! ...

so we can determine the first one by its period and remove the result element from the set and keep doing for the rest n-1 elements

	class Solution {
	public:
	    string getPermutation(int n, int k) {
	        // for m th digit, the period is (n -1) !
	        vector<int> periods(n, 1);
	        for (int i = 1; i < periods.size(); ++i)
	        {
	            periods[i] = periods[i-1] * i;
	        }
	        
	        vector<int> cands;
	        for (int i = 1; i <= n; ++i)
	        {
	            cands.push_back(i);
	        }
	        
	        string result;
	        k = k - 1;
	        for (int i = periods.size() - 1; i >= 0; --i)
	        {
	            int idx = k / periods[i];
	            k %= periods[i];
	            result.append(1, cands[idx] + '0');
	            cands.erase(cands.begin() + idx);
	        }
	        
	        return result;
	    }
	};