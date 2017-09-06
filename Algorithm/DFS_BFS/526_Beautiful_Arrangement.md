### Beautiful Arrangement
Suppose you have N integers from 1 to N. We define a beautiful arrangement as an array that is constructed by these N numbers successfully if one of the following is true for the ith position (1 <= i <= N) in this array:

The number at the ith position is divisible by i.
i is divisible by the number at the ith position.
Now given N, how many beautiful arrangements can you construct?

Example 1:
Input: 2
Output: 2
Explanation: 

The first beautiful arrangement is [1, 2]:

Number at the 1st position (i=1) is 1, and 1 is divisible by i (i=1).

Number at the 2nd position (i=2) is 2, and 2 is divisible by i (i=2).

The second beautiful arrangement is [2, 1]:

Number at the 1st position (i=1) is 2, and 2 is divisible by i (i=1).

Number at the 2nd position (i=2) is 1, and i (i=2) is divisible by 1.
Note:
N is a positive integer and will not exceed 15.

[leetcode](https://leetcode.com/problems/beautiful-arrangement/description/)

### Answer
Since it will not exceed five, we can list all possible for each number and use dfs. 

class Solution {
public:
    int countArrangement(int N) {
        vector<bool> visited(N + 1, false);
        return dfs(1, visited);
    }
    
    int dfs(int i, vector<bool> &visited)
    {
        if (i >= visited.size()) return 1;
        int result = 0;
        for (int j = 1; j < visited.size(); ++j)
        {
            if (!visited[j] && ( j % i == 0 || i % j == 0) )
            {
                visited[j] = true;
                result += dfs(i + 1, visited);
                visited[j] = false;
            }
        }
        
        return result;
    }
};
