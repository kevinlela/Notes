### Data Stream as Disjoint Intervals
Given a data stream input of non-negative integers a1, a2, ..., an, ..., summarize the numbers seen so far as a list of disjoint intervals.

For example, suppose the integers from the data stream are 1, 3, 7, 2, 6, ..., then the summary will be:

[1, 1]
[1, 1], [3, 3]
[1, 1], [3, 3], [7, 7]
[1, 3], [7, 7]
[1, 3], [6, 7]
Follow up:
What if there are lots of merges and the number of disjoint intervals are small compared to the data stream's size?


[leetcode](https://leetcode.com/problems/data-stream-as-disjoint-intervals/description/)

### Answer
	/**
	 * Definition for an interval.
	 * struct Interval {
	 *     int start;
	 *     int end;
	 *     Interval() : start(0), end(0) {}
	 *     Interval(int s, int e) : start(s), end(e) {}
	 * };
	 */
	class SummaryRanges {
	public:
	    /** Initialize your data structure here. */
	    SummaryRanges() {
	        
	    }
	    
	    void addNum(int val) {
	        Interval nitv(val, val);
	        if (d_itv.empty())
	        {
	            d_itv.insert(nitv);
	            return;
	        }
	        
	        auto lower_b = d_itv.lower_bound(nitv);
	        auto rb = lower_b;
	        auto lb = lower_b;
	        
	        
	        // iterate to the left
	        if (lb != d_itv.begin())
	        {
	            --lb;
	            bool should_break = false;
	            for (auto iter = lb; ;)
	            {
	                auto next = iter;
	                if (next != d_itv.begin()) --next;
	                else should_break = true;
	                if (iter->end >= nitv.start - 1)
	                {
	                    nitv.start = min(nitv.start, iter->start);
	                    nitv.end = max(nitv.end, iter->end);
	                    d_itv.erase(iter);
	                }
	                else break;

	                if (should_break) break;
	                iter = next;
	            }
	        }
	        
	        // iterate to the right
	        for (auto iter = rb; iter != d_itv.end(); )
	        {
	            auto next = iter;
	            ++next;
	            //cout << iter->start << " " << iter->end << endl;
	            if (iter->start <= nitv.end + 1)
	            {
	                nitv.end = max(nitv.end, iter->end);
	                d_itv.erase(iter);
	            }
	            else break;
	            iter = next;
	        }
	        
	        d_itv.insert(nitv);
	    }
	    
	    vector<Interval> getIntervals() {
	        vector<Interval> result;
	        for (auto iter = d_itv.begin(); iter != d_itv.end(); ++iter)
	        {
	            result.push_back(*iter);
	        }
	        return result;
	    }
	private:
	    struct less_than{
	      inline bool operator () (const Interval &itv1, const Interval &itv2)
	      {
	          return itv1.start < itv2.start;
	      }
	    };
	    set<Interval, less_than> d_itv;
	};

	/**
	 * Your SummaryRanges object will be instantiated and called as such:
	 * SummaryRanges obj = new SummaryRanges();
	 * obj.addNum(val);
	 * vector<Interval> param_2 = obj.getIntervals();
	 */