### Happy Number
Write an algorithm to determine if a number is "happy".

A happy number is a number defined by the following process: Starting with any positive integer, replace the number by the sum of the squares of its digits, and repeat the process until the number equals 1 (where it will stay), or it loops endlessly in a cycle which does not include 1. Those numbers for which this process ends in 1 are happy numbers.

Example: 19 is a happy number

12 + 92 = 82

82 + 22 = 68

62 + 82 = 100

12 + 02 + 02 = 1

[leetcode](https://leetcode.com/problems/happy-number/description/)

### Answer 
This is the same as [141](141_Linked_List_Cycle.md).

	class Solution {
	public:
	    bool isHappy(int n) {
	        int slow = n, fast = n;
	        
	        do 
	        {
	            slow = nextHappy(slow);
	            fast = nextHappy(fast);
	            fast = nextHappy(fast);
	        }while (slow != fast);
	        
	        return slow == 1;
	    }
	    
	    int nextHappy(int n)
	    {
	        int result = 0;
	        while (n)
	        {
	            int digit = n % 10;
	            result += digit * digit;
	            n /= 10;
	        }
	        return result;
	    }
	};