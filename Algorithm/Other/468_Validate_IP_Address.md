### Validate IP Address
Write a function to check whether an input string is a valid IPv4 address or IPv6 address or neither.

IPv4 addresses are canonically represented in dot-decimal notation, which consists of four decimal numbers, each ranging from 0 to 255, separated by dots ("."), e.g.,172.16.254.1;

Besides, leading zeros in the IPv4 is invalid. For example, the address 172.16.254.01 is invalid.

IPv6 addresses are represented as eight groups of four hexadecimal digits, each group representing 16 bits. The groups are separated by colons (":"). For example, the address 2001:0db8:85a3:0000:0000:8a2e:0370:7334 is a valid one. Also, we could omit some leading zeros among four hexadecimal digits and some low-case characters in the address to upper-case ones, so 2001:db8:85a3:0:0:8A2E:0370:7334 is also a valid IPv6 address(Omit leading zeros and using upper cases).

However, we don't replace a consecutive group of zero value with a single empty group using two consecutive colons (::) to pursue simplicity. For example, 2001:0db8:85a3::8A2E:0370:7334 is an invalid IPv6 address.

Besides, extra leading zeros in the IPv6 is also invalid. For example, the address 02001:0db8:85a3:0000:0000:8a2e:0370:7334 is invalid.

Note: You may assume there is no extra space or special characters in the input string.

Example 1:
Input: "172.16.254.1"

Output: "IPv4"

Explanation: This is a valid IPv4 address, return "IPv4".
Example 2:
Input: "2001:0db8:85a3:0:0:8A2E:0370:7334"

Output: "IPv6"

Explanation: This is a valid IPv6 address, return "IPv6".
Example 3:
Input: "256.256.256.256"

Output: "Neither"

Explanation: This is neither a IPv4 address nor a IPv6 address.

[leetcode](https://leetcode.com/problems/validate-ip-address/description/)

### Answer

	class Solution {
	public:
	    string validIPAddress(string IP) {
	        string neither("Neither");
	        string ipv4("IPv4");
	        string ipv6("IPv6");
	        
	        int numOfGroups = 0;
	        bool v4 = true, v6 = true;
	        string group;
	        char prev = 0;
	        for (int i = 0; i < IP.size(); ++i)
	        {
	            if (IP[i] == ' ') continue; // allow space
	            if (IP[i] == '.')
	            {
	                if (v6 == true && v4 == false) return neither; // previous is v6 but now change to v4 
	                if ( !isValidV4Group(group) ) return neither;
	                v6 = false;
	                ++numOfGroups;
	                if (numOfGroups >= 4) return neither;
	                group.clear();
	            }
	            else if (IP[i] == ':')
	            {
	                if (v4 == true && v6 == false) return neither;
	                if ( !isValidV6Group(group) ) return neither;
	                v4 = false;
	                ++numOfGroups;
	                if (numOfGroups >= 8) return neither;
	                group.clear();
	            }
	            else if (!isalnum(IP[i])) return neither;
	            else if (tolower(IP[i]) > 'f') return neither;
	            else group.append(1, IP[i]);
	            if (group.size() > 4) return neither;
	        }
	        
	        if (v4)
	        {
	            if (numOfGroups != 3) return neither;
	            if ( !isValidV4Group(group) ) return neither;
	            return ipv4;
	        }
	        else if (v6)
	        {
	            if (numOfGroups != 7) return neither;
	            //cout << "pass else if v6" << endl;
	            if ( !isValidV6Group(group) ) return neither;
	            return ipv6;
	        }
	        
	        return neither;
	    }
	    
	    bool isValidV4Group(const string &group)
	    {
	        //cout << group << "|" << group.size() << endl;
	        if (group.size() > 3) return false;
	        if (group.size() == 0) return false;
	        if (group[0] == '0' && group.size() != 1) return false;
	        int val = 0;
	        for (int i = 0; i < group.size(); ++i)
	        {
	            ///cout << group[i] << " " << (int)isdigit(group[i]) << endl;
	            if (!isdigit(group[i])) return false;
	            val = val*10 + group[i] - '0';
	        }
	        if (val > 255) return false;
	        //cout << "pass" << endl;
	        return true;
	    }
	    
	    bool isValidV6Group(const string &group)
	    {
	        if (group.size() > 4) return false;
	        if (group.size() == 0) return false;
	        return true;
	    }
	};