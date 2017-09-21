### Find the Celebrity
Suppose you are at a party with n people (labeled from 0 to n - 1) and among them, there may exist one celebrity. The definition of a celebrity is that all the other n - 1 people know him/her but he/she does not know any of them.

Now you want to find out who the celebrity is or verify that there is not one. The only thing you are allowed to do is to ask questions like: "Hi, A. Do you know B?" to get information of whether A knows B. You need to find out the celebrity (or verify there is not one) by asking as few questions as possible (in the asymptotic sense).

You are given a helper function bool knows(a, b) which tells you whether A knows B. Implement a function int findCelebrity(n), your function should minimize the number of calls to knows.

Note: There will be exactly one celebrity if he/she is in the party. Return the celebrity's label if there is a celebrity in the party. If there is no celebrity, return -1.

[leetcode](https://leetcode.com/problems/find-the-celebrity/description/)

### Answer

Tricky solution O(N). The first iteration uses greedy algorithm to find the only one candidates. 

	// Forward declaration of the knows API.
	bool knows(int a, int b);

	class Solution {
	public:
	    int findCelebrity(int n) {
	        if (n == 0) return -1;
	        int cand = 0;
	        for (int i = 1; i < n; ++i)
	        {
	            if (knows(cand, i)) cand = i;
	        }
	        
	        for (int i = 0; i < n; ++i)
	        {
	            if (cand == i) continue;
	            if (knows(cand, i) || !knows(i, cand)) return -1;
	        }
	        
	        return cand;
	    }
	};

optimized brutal force solution

	// Forward declaration of the knows API.
	bool knows(int a, int b);

	class Solution {
	public:
	    int findCelebrity(int n) {
	        if (n == 0) return -1;
	        vector<bool> cand(n, true);
	        for (int i = 0; i < n; ++i)
	        {
	            if (cand[i] == false) continue;
	            for (int j = 0; j < n; ++j)
	            {
	                if (i == j) continue;
	                if (!knows(i, j)) cand[j] = false;
	                else cand[i] = false;
	                if (!knows(j, i)) cand[i] = false;
	                else cand[j] = false;
	                if (cand[i] == false) break;
	            }
	            if (cand[i]) return i;
	        }
	        if (cand[n-1]) return n-1;
	        return -1;
	    }
	};