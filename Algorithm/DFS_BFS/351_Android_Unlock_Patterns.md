### Android Unlock Patterns
Given an Android 3x3 key lock screen and two integers m and n, where 1 ≤ m ≤ n ≤ 9, count the total number of unlock patterns of the Android lock screen, which consist of minimum of m keys and maximum n keys.

Rules for a valid pattern:
Each pattern must connect at least m keys and at most n keys.
All the keys must be distinct.
If the line connecting two consecutive keys in the pattern passes through any other keys, the other keys must have previously selected in the pattern. No jumps through non selected key is allowed.
The order of keys used matters.

Explanation:
| 1 | 2 | 3 |
| 4 | 5 | 6 |
| 7 | 8 | 9 |
Invalid move: 4 - 1 - 3 - 6 
Line 1 - 3 passes through key 2 which had not been selected in the pattern.

Invalid move: 4 - 1 - 9 - 2
Line 1 - 9 passes through key 5 which had not been selected in the pattern.

Valid move: 2 - 4 - 1 - 3 - 6
Line 1 - 3 is valid because it passes through key 2, which had been selected in the pattern

Valid move: 6 - 5 - 4 - 1 - 9 - 2
Line 1 - 9 is valid because it passes through key 5, which had been selected in the pattern.

Example:
Given m = 1, n = 1, return 9.

Credits:
Special thanks to @elmirap for adding this problem and creating all test cases.

[leetcode](https://leetcode.com/problems/android-unlock-patterns/description/)

### Answer
The case 1->8 does not pass 4 and 5. It is unclear in the description

	class Solution {
	public:
	    int numberOfPatterns(int m, int n) {
	        int result = 0;
	        vector<bool> visited(10, false);
	        recur(visited, result, 0, 0, m, n);
	        return result;
	    }
	    
	    void recur(vector<bool> &visited, int &result, int curr, int k, int m, int n)
	    {
	        if (k >= m ) ++result;
	        if (k == n) return;
	        for (int i = 1; i <= 9; ++i)
	        {
	            if (visited[i]) continue;
	            
	            vector<int> pass = getPassThrough(curr, i);
	            bool canPass = true;
	            for (int p = 0; p < pass.size(); ++p)
	            {
	                canPass &= visited[pass[p]];
	            }
	            if (!canPass) continue;

	            visited[i] = true;
	            recur(visited, result, i, k+1, m, n);
	            visited[i] = false;
	        }
	    }
	    
	    vector<int> getPassThrough(int p1, int p2)
	    {
	        if (p1 == p2) return vector<int>();
	        if (p1 > p2) return getPassThrough(p2, p1);
	        
	        if (p1 == 1)
	        {
	            if (p2 == 2 || p2 == 4 || p2 == 5) return {};
	            if (p2 == 3) return {2};
	            if (p2 == 7) return {4};
	            if (p2 == 9) return {5};
	            //if (p2 == 6) return {2, 5};
	            //if (p2 == 8) return {4, 5};
	        }
	        if (p1 == 2)
	        {
	            if (p2 == 3 || p2 == 4 || p2 == 5 || p2 == 6) return {};
	            if (p2 == 8) return {5};
	            //if (p2 == 7) return {4, 5};
	            //if (p2 == 9) return {5, 6};
	        }
	        if (p1 == 3)
	        {
	            if (p2 == 5 || p2 == 6) return {};
	            if (p2 == 7) return {5};
	            if (p2 == 9) return {6};
	            //if (p2 == 4) return {2, 5};
	            //if (p2 == 8) return {5, 6};
	        }
	        if (p1 == 4)
	        {
	            if (p2 == 5 || p2 == 7 || p2 == 8) return {};
	            if (p2 == 6) return {5};
	            //if (p2 == 9) return {5, 8};
	        }
	        if (p1 == 5) return {};
	        if (p1 == 6)
	        {
	            if (p2 == 8 || p2 == 9) return {};
	            //if (p2 == 7) return {5, 8};
	        }
	        if (p1 == 7)
	        {
	            if (p2 == 8) return {};
	            if (p2 == 9) return {8};
	        }
	        
	        return {};
	    }
	};