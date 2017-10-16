### 4 Keys Keyboard
Imagine you have a special keyboard with the following keys:

Key 1: (A): Print one 'A' on screen.

Key 2: (Ctrl-A): Select the whole screen.

Key 3: (Ctrl-C): Copy selection to buffer.

Key 4: (Ctrl-V): Print buffer on screen appending it after what has already been printed.

Now, you can only press the keyboard for N times (with the above four keys), find out the maximum numbers of 'A' you can print on screen.

Example 1:
Input: N = 3
Output: 3
Explanation: 
We can at most get 3 A's on screen by pressing following key sequence:
A, A, A
Example 2:
Input: N = 7
Output: 9
Explanation: 
We can at most get 9 A's on screen by pressing following key sequence:
A, A, A, Ctrl A, Ctrl C, Ctrl V, Ctrl V
Note:
1 <= N <= 50
Answers will be in the range of 32-bit signed integer.

[leetcode](https://leetcode.com/problems/4-keys-keyboard/description/)

### Answer
The key here, since we can have consecutive V so we need to cover all cases. 

	class Solution {
	public:
	    int maxA(int N) {
	        vector<int> A(N+1, 0);
	        vector<int> V(N+1, 0);
	        vector<int> R(N+1, 0);
	        
	        for (int i = 1; i <= N; ++i)
	        {
	            A[i] = max(A[i-1], V[i-1]) + 1;
	            for (int j = 3; j <= i; ++j)
	            {
	                V[i] = max(V[i], R[j-3]*(i - j + 2));
	            }
	            R[i] = max(A[i], V[i]);
	        }
	        
	        return R[N];
	    }
	};