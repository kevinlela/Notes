### Sequence Reconstruction
Check whether the original sequence org can be uniquely reconstructed from the sequences in seqs. The org sequence is a permutation of the integers from 1 to n, with 1 ≤ n ≤ 104. Reconstruction means building a shortest common supersequence of the sequences in seqs (i.e., a shortest sequence so that all sequences in seqs are subsequences of it). Determine whether there is only one sequence that can be reconstructed from seqs and it is the org sequence.

Example 1:

Input:
org: [1,2,3], seqs: [[1,2],[1,3]]

Output:
false

Explanation:
[1,2,3] is not the only one sequence that can be reconstructed, because [1,3,2] is also a valid sequence that can be reconstructed.
Example 2:

Input:
org: [1,2,3], seqs: [[1,2]]

Output:
false

Explanation:
The reconstructed sequence can only be [1,2].
Example 3:

Input:
org: [1,2,3], seqs: [[1,2],[1,3],[2,3]]

Output:
true

Explanation:
The sequences [1,2], [1,3], and [2,3] can uniquely reconstruct the original sequence [1,2,3].
Example 4:

Input:
org: [4,1,5,2,6,3], seqs: [[5,2,6,3],[4,1,5,2]]

Output:
true
UPDATE (2017/1/8):
The seqs parameter had been changed to a list of list of strings (instead of a 2d array of strings). Please reload the code definition to get the latest changes.

[leetcode](https://leetcode.com/problems/sequence-reconstruction/description/)

### Answer

	class Solution {
	public:
	    bool sequenceReconstruction(vector<int>& org, vector<vector<int>>& seqs) {
	        // we cannot use topological sort since, we may have duplicate chars in orgs which are also valid
	        // say
	        // org: [3,1,2,3]
	        // seqs: [[1,2],[2,3],[3,1]]
	        // since it is unique, we do not need to care whether it is shortest
	        // first, detect if all subseq exist in org
	        // second, consecutive pair in org must exist in seqs
	        vector<int> iter(seqs.size(), 0);
	        unordered_map<int, int> count;
	        for (int i = 0; i < org.size(); ++i)
	        {
	            ++count[org[i]];
	            for (int j = 0; j < iter.size(); ++j)
	            {
	                if (iter[j] == seqs[j].size()) continue;
	                if (seqs[j][iter[j]] == org[i]) 
	                {
	                    --count[org[i]];
	                    ++iter[j];
	                }
	            }
	        }
	        
	        for (auto iter = count.begin(); iter != count.end(); ++iter)
	        {
	            if (iter->second > 0) return false;
	        }
	        
	        for (int i = 0; i < seqs.size(); ++i)
	        {
	            if (iter[i] != seqs[i].size()) return false;
	            iter[i] = 0;
	        }
	        
	        for (int i = 0; i < (int)org.size() - 1; ++i)
	        {
	            int curr = org[i], next = org[i+1];
	            bool found = false;
	            for(int j = 0; j < seqs.size(); ++j)
	            {
	                if (iter[j] >= (int)seqs[j].size() - 1) continue;
	                if (seqs[j][iter[j]] == curr)
	                {
	                    if (seqs[j][iter[j] + 1] == next) found = true;
	                    ++iter[j];
	                }
	            }
	            if (found == false) return false;
	        }
	        
	        return true;
	    }
	};
