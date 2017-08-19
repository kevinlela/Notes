### Minimum Genetic Mutation
A gene string can be represented by an 8-character long string, with choices from "A", "C", "G", "T".

Suppose we need to investigate about a mutation (mutation from "start" to "end"), where ONE mutation is defined as ONE single character changed in the gene string.

For example, "AACCGGTT" -> "AACCGGTA" is 1 mutation.

Also, there is a given gene "bank", which records all the valid gene mutations. A gene must be in the bank to make it a valid gene string.

Now, given 3 things - start, end, bank, your task is to determine what is the minimum number of mutations needed to mutate from "start" to "end". If there is no such a mutation, return -1.

Note:

Starting point is assumed to be valid, so it might not be included in the bank.
If multiple mutations are needed, all mutations during in the sequence must be valid.
You may assume start and end string is not the same.
Example 1:

start: "AACCGGTT"
end:   "AACCGGTA"
bank: ["AACCGGTA"]

return: 1
Example 2:

start: "AACCGGTT"
end:   "AAACGGTA"
bank: ["AACCGGTA", "AACCGCTA", "AAACGGTA"]

return: 2
Example 3:

start: "AAAAACCC"
end:   "AACCCCCC"
bank: ["AAAACCCC", "AAACCCCC", "AACCCCCC"]

return: 3


[leetcode](https://leetcode.com/problems/minimum-genetic-mutation/description/)

### Answer 
Use DFS. However, since it is 8 chars and 4 choose, it is a 32 bit integer. To detect whether it is an 1 bit difference n&(n-1) = 0

	class Solution {
	public:
	    int minMutation(string start, string end, vector<string>& bank) {
	        if (start == end) return 0;
	        
	        int len = bank.size();
	        vector<vector<int>> neis(len, vector<int>());
	        
	        int target = -1;
	        for (int i = 0; i < len; ++i)
	        {
	            if (bank[i] == end)
	            {
	                target = i;
	                break;
	            }
	        }
	        if (target == -1) return -1;
	        
	        for (int j = 0; j < len; ++j)
	        {
	            for (int i = j + 1; i < len; ++i)
	            {
	                if (isMutation(bank[j], bank[i]))
	                {
	                    neis[j].push_back(i);
	                    neis[i].push_back(j);
	                }
	            }
	        }
	        
	        queue<int> myQ;
	        vector<bool> visited(len, false);
	        int minStep = 1;
	        
	        for (int i = 0; i < len; ++i)
	        {
	            if (isMutation(bank[i], start))
	            {
	                myQ.push(i);
	                visited[i] = true;
	                if (i == target) return minStep;
	            }
	        }
	        
	        while (!myQ.empty())
	        {
	            int qLen = myQ.size();
	            ++minStep;
	            
	            for (int i = 0; i < qLen; ++i)
	            {
	                int curr = myQ.front();
	                for (int j = 0; j < neis[curr].size(); ++j)
	                {
	                    int neiIdx = neis[curr][j];
	                    if (visited[neiIdx] == false)
	                    {
	                        myQ.push(neiIdx);
	                        visited[neiIdx] = true;
	                        if (neiIdx == target) return minStep;
	                    }
	                }
	                myQ.pop();
	            }
	        }
	        
	        return -1;
	    }
	    
	    bool isMutation(const string &s1, const string &s2)
	    {
	        int count = 0, len1 = s1.size(), len2 = s2.size();
	        if (len1 != len2) return false;
	        for (int k = 0; k < len1; ++k)
	        {
	            if (s1[k] != s2[k]) ++count;
	            if (count > 1) return false;
	        }
	        return count == 1;
	    }
	    
	};