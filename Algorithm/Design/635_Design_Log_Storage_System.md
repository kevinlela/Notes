### Design Log Storage System
You are given several logs that each log contains a unique id and timestamp. Timestamp is a string that has the following format: Year:Month:Day:Hour:Minute:Second, for example, 2017:01:01:23:59:59. All domains are zero-padded decimal numbers.

Design a log storage system to implement the following functions:

void Put(int id, string timestamp): Given a log's unique id and timestamp, store the log in your storage system.


int[] Retrieve(String start, String end, String granularity): Return the id of logs whose timestamps are within the range from start to end. Start and end all have the same format as timestamp. However, granularity means the time level for consideration. For example, start = "2017:01:01:23:59:59", end = "2017:01:02:23:59:59", granularity = "Day", it means that we need to find the logs within the range from Jan. 1st 2017 to Jan. 2nd 2017.

Example 1:
put(1, "2017:01:01:23:59:59");
put(2, "2017:01:01:22:59:59");
put(3, "2016:01:01:00:00:00");
retrieve("2016:01:01:01:01:01","2017:01:01:23:00:00","Year"); // return [1,2,3], because you need to return all logs within 2016 and 2017.
retrieve("2016:01:01:01:01:01","2017:01:01:23:00:00","Hour"); // return [1,2], because you need to return all logs start from 2016:01:01:01 to 2017:01:01:23, where log 3 is left outside the range.
Note:
There will be at most 300 operations of Put or Retrieve.
Year ranges from [2000,2017]. Hour ranges from [00,23].
Output for Retrieve has no order required.

[leetcode](https://leetcode.com/problems/design-log-storage-system/description/)

### Answer
	class LogSystem {
	public:
	    LogSystem() {
	        d_gra_s["Year"]  = "01:01:00:00:00";
	        d_gra_e["Year"]  = "12:31:23:59:59";
	        d_gra_s["Month"] = "01:00:00:00";
	        d_gra_e["Month"] = "31:23:59:59";
	        d_gra_s["Day"]   = "00:00:00";
	        d_gra_e["Day"]   = "23:59:59";
	        d_gra_s["Hour"]  = "00:00";
	        d_gra_e["Hour"]  = "59:59";
	        d_gra_s["Minute"]= "00";
	        d_gra_e["Minute"]= "59";
	        d_gra_s["Second"]= "";
	        d_gra_s["Second"]= "";
	    }
	    
	    void put(int id, string timestamp) {
	        d_logs[timestamp] = id;
	    }
	    
	    vector<int> retrieve(string s, string e, string gra) {
	        int len = s.size();
	        string& sr = d_gra_s[gra];
	        string& er = d_gra_e[gra];
	        s.replace(len-sr.size(), sr.size(), sr);
	        e.replace(len-er.size(), er.size(), er);
	        
	        auto lb = d_logs.lower_bound(s);
	        auto ub = d_logs.upper_bound(e);
	        
	        vector<int> result;
	        for (auto it = lb; it != ub; ++it)
	            result.push_back(it->second);
	        return result;
	    }
	    
	    void setGra(string &s, int gra)
	    {
	        for (int i = 5; i < s.size(); ++i)
	        {
	            if (i >= gra && isdigit(s[i])) s[i] = '0';
	        }
	    }
	private:
	    map<string, int> d_logs;
	    unordered_map<string, string> d_gra_s;
	    unordered_map<string, string> d_gra_e;
	};

	/**
	 * Your LogSystem object will be instantiated and called as such:
	 * LogSystem obj = new LogSystem();
	 * obj.put(id,timestamp);
	 * vector<int> param_2 = obj.retrieve(s,e,gra);
	 */