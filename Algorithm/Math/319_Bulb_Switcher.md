### Bulb Switcher
There are n bulbs that are initially off. You first turn on all the bulbs. Then, you turn off every second bulb. On the third round, you toggle every third bulb (turning on if it's off or turning off if it's on). For the ith round, you toggle every i bulb. For the nth round, you only toggle the last bulb. Find how many bulbs are on after n rounds.

Example:

Given n = 3. 

At first, the three bulbs are [off, off, off].
After first round, the three bulbs are [on, on, on].
After second round, the three bulbs are [on, off, on].
After third round, the three bulbs are [on, off, off]. 

So you should return 1, because there is only one bulb is on.

[leetcode](https://leetcode.com/problems/bulb-switcher/description/)

### Answer 
The bulb switches at its factor. Factors are paired. like if you have 2 as factor, you mush have x/2 as the other. Two factors are different except the power one. 

	class Solution {
	public:
	    int bulbSwitch(int n) {
	        // every bulb get toggle at its factors
	        // the number of factor is always even
	        // even leads to off
	        // execept x^2 has odd number of factors
	        
	        return sqrt(n);
	    }
	};