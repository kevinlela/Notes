### Find Median from Data Stream
Median is the middle value in an ordered integer list. If the size of the list is even, there is no middle value. So the median is the mean of the two middle value.

Examples: 
[2,3,4] , the median is 3

[2,3], the median is (2 + 3) / 2 = 2.5

Design a data structure that supports the following two operations:

void addNum(int num) - Add a integer number from the data stream to the data structure.
double findMedian() - Return the median of all elements so far.
For example:

addNum(1)
addNum(2)
findMedian() -> 1.5
addNum(3) 
findMedian() -> 2

[leetcode](https://leetcode.com/problems/find-median-from-data-stream/description/)

### Answer 
We maintain two priority queue, one from small to large, the other from large to small so we can maintain two top elements according to their size. 

	class MedianFinder {
	public:
	    struct greater_than{
	        inline bool operator() (const int &a, const int &b)
	        {
	            return a > b;
	        }
	    };
	    /** initialize your data structure here. */
	    MedianFinder() {
	        
	    }
	    
	    void addNum(int num) {
	        if (q1.empty())
	        {
	            q1.push(num);
	        }
	        else if (num < q1.top())
	        {
	            q1.push(num);
	            if (q1.size() > q2.size() + 1)
	            {
	                q2.push(q1.top());
	                q1.pop();
	            }
	        }
	        else
	        {
	            q2.push(num);
	            if (q1.size() < q2.size())
	            {
	                q1.push(q2.top());
	                q2.pop();
	            }
	        }
	        
	        
	    }
	    
	    double findMedian() {
	        if (q1.size() > q2.size()) return q1.top();
	        return ((double)(q1.top() + q2.top())) / 2;
	    }
	    
	private:
	    priority_queue<int> q1; //rank ascendingly
	    priority_queue<int, vector<int>, greater_than> q2; //rank descendingly
	};

	/**
	 * Your MedianFinder object will be instantiated and called as such:
	 * MedianFinder obj = new MedianFinder();
	 * obj.addNum(num);
	 * double param_2 = obj.findMedian();
	 */