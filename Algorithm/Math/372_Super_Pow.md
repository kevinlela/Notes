### Super Pow
Your task is to calculate ab mod 1337 where a is a positive integer and b is an extremely large positive integer given in the form of an array.

Example1:

a = 2
b = [3]

Result: 8
Example2:

a = 2
b = [1,0]

Result: 1024

[leetcode](https://leetcode.com/problems/super-pow/description/)

### Answer

The only challenge is to know the property (a*b) % c = ((a%c) * (b%c))%c

	class Solution {
	public:
	    int superPow(int a, vector<int>& b) {
	        // a^b mod 1337
	        // property (a*b) % c = ((a%c) * (b%c))%c
	        int len = b.size();
	        if (len == 0) return 1;
	        vector<int> mods(len, 0);
	        int base = a % 1337;
	        for (int i = len - 1; i >= 0; --i)
	        {
	            mods[i] = getMod(base, b[i]);
	            if (i != 0) base = getMod(base, 10);
	        }
	        
	        int result = mods[0];
	        for (int i = 1; i < len; ++i)
	        {
	            result = (result * mods[i]) % 1337;
	        }
	        
	        return result;
	    }
	    
	    // this get a^p % 1337, where base = a % 1337
	    int getMod(int base, int power)
	    {
	        if (power == 0) return 1;
	        int result = base;
	        for (int i = 1; i < power; ++i)
	        {
	            result = (result * base) % 1337;
	        }
	        return result;
	    }
	};
