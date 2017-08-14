### Count Primes
Description:

Count the number of prime numbers less than a non-negative number, n.

[leetcode](https://leetcode.com/problems/count-primes/description/)

### Answer 
We can gray out all a*x when we visit x. There are two trickes, 
* first, we just need to start at a = x when meeting x, because element < x*x is handled by the previous element
* we just need to check x <= sqrt[n] since x > sqrt[n] will mark > than n 

	class Solution {
	public:
	    int countPrimes(int n) {
	        // 1 is a primes number
	        if (n <= 2) return 0;
	        vector<bool> visited(n, false);
	        int result = 1; //include 2
	        int sq = sqrt(n); // after this number, we do not need to calculate prime mutiplication
	        for (int k = 3; k < n; k += 2)
	        {
	            if (visited[k] == false) ++result;
	            for (int j = k * k; k <= sq && j < n; j += k)
	            {
	                visited[j] = true;
	            }
	        }
	        
	        return result;
	    }
	};