### Moving Average from Data Stream
Given a stream of integers and a window size, calculate the moving average of all integers in the sliding window.

For example,
MovingAverage m = new MovingAverage(3);
m.next(1) = 1
m.next(10) = (1 + 10) / 2
m.next(3) = (1 + 10 + 3) / 3
m.next(5) = (10 + 3 + 5) / 3

[leetcode](https://leetcode.com/problems/moving-average-from-data-stream/description/)

### Answer
	class MovingAverage {
	public:
	    /** Initialize your data structure here. */
	    MovingAverage(int size) {
	        d_size = size;
	        d_curr = 0;
	    }
	    
	    double next(int val) {
	        if (d_size == 0) return 0;
	        else if (d_q.size() < d_size) 
	        {
	            d_curr = (d_curr*(double)(d_q.size()) + (double)val)/(double)(d_q.size() + 1);       
	            d_q.push(val);
	        }
	        else
	        { 
	            d_curr -= (double)(d_q.front())/(double)d_size;
	            d_curr += (double)val/(double)d_size;
	            d_q.pop();
	            d_q.push(val);
	        }
	        return d_curr;
	    }
	private:
	    int d_size;
	    double d_curr;
	    queue<int> d_q;
	};

	/**
	 * Your MovingAverage object will be instantiated and called as such:
	 * MovingAverage obj = new MovingAverage(size);
	 * double param_1 = obj.next(val);
	 */