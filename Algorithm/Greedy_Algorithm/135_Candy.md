### Candy
There are N children standing in a line. Each child is assigned a rating value.

You are giving candies to these children subjected to the following requirements:

* Each child must have at least one candy.
* Children with a higher rating get more candies than their neighbors.
What is the minimum candies you must give?

[leetcode](https://leetcode.com/problems/candy/description/)

### Answer 
Greedy Algorithm. We can always increment by 1 when the rating is monotonically increasing, once it decreases, we can temporily set this to be 1 and increment it if the next one keeps decreasing. once the decreasing length is too long, we need to increase the previous peak value accordingly. 

A good question is to ask what about equal value? for this case, equal value can be regard either greater or smaller. 

	class Solution {
	public:
	    int candy(vector<int>& ratings) {
	        // there are two cases: up-ward and down-ward
	        // the start-point of up-ward must be 1 candy
	        // the down-ward is tricky, say s[i] is the peak value, it can hold s[i] elements afterwards by decreasing by 1 for each element
	        // once the s[i+1] exceed the s[i] we need to increase s[i]
	        // what about equal? equal can be considered as either upward or down-ward
	        // for example [5, 5, 5, 5, 4] get 6 candies in total
	        if (ratings.size() == 0) return 0;
	        
	        int peak = 0, peakCandy = 1, prevCandy = 1, totalCandy = 1; // set the first element to be 1 and set it to be peak
	        
	        for (int k = 1; k < ratings.size(); ++k)
	        {
	            if (ratings[k] > ratings[k-1])
	            {
	                peak = k;
	                peakCandy = (++prevCandy);
	                totalCandy += prevCandy;
	            }
	            else if (ratings[k] < ratings[k-1])
	            {
	                totalCandy += (k - peak);
	                if (k - peak >= peakCandy) totalCandy += 1; 
	                prevCandy = 1;
	            }
	            else // if (ratings[k] == ratings[k-1]) we reset everything
	            {
	                totalCandy += 1;
	                peak = k;
	                peakCandy = 1;
	                prevCandy = 1;
	            }
	        }
	        
	        return totalCandy;
	    }
	};