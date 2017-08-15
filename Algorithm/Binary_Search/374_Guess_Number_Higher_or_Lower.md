### Guess Number Higher or Lower
We are playing the Guess Game. The game is as follows:

I pick a number from 1 to n. You have to guess which number I picked.

Every time you guess wrong, I'll tell you whether the number is higher or lower.

You call a pre-defined API guess(int num) which returns 3 possible results (-1, 1, or 0):

-1 : My number is lower
 1 : My number is higher
 0 : Congrats! You got it!
Example:
n = 10, I pick 6.

Return 6.

[leetcode](https://leetcode.com/problems/guess-number-higher-or-lower/description/)

### Answer
	// Forward declaration of guess API.
	// @param num, your guess
	// @return -1 if my number is lower, 1 if my number is higher, otherwise return 0
	int guess(int num);

	class Solution {
	public:
	    int guessNumber(int n) {
	        int st = 1, ed = n;
	        while (st <= ed)
	        {
	            int mid = st + (ed - st) / 2;
	            int res = guess(mid);
	            if (res == 0) return mid;
	            else if (res == 1) st = mid + 1;
	            else ed = mid - 1;
	        }
	        
	        return 0;
	    }
	};