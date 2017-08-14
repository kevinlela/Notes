### Integer to English Words
Convert a non-negative integer to its english words representation. Given input is guaranteed to be less than 231 - 1.

For example,
123 -> "One Hundred Twenty Three"
12345 -> "Twelve Thousand Three Hundred Forty Five"
1234567 -> "One Million Two Hundred Thirty Four Thousand Five Hundred Sixty Seven"

[leetcode](https://leetcode.com/problems/integer-to-english-words/description/)

### Answer 

class Solution {
public:
    Solution (){
        d_eng_1_9.push_back("One");
        d_eng_1_9.push_back("Two");
        d_eng_1_9.push_back("Three");
        d_eng_1_9.push_back("Four");
        d_eng_1_9.push_back("Five");
        d_eng_1_9.push_back("Six");
        d_eng_1_9.push_back("Seven");
        d_eng_1_9.push_back("Eight");
        d_eng_1_9.push_back("Nine");
        
        d_eng_11_19.push_back("Eleven");
        d_eng_11_19.push_back("Twelve");
        d_eng_11_19.push_back("Thirteen");
        d_eng_11_19.push_back("Fourteen");
        d_eng_11_19.push_back("Fifteen");
        d_eng_11_19.push_back("Sixteen");
        d_eng_11_19.push_back("Seventeen");
        d_eng_11_19.push_back("Eighteen");
        d_eng_11_19.push_back("Nineteen");
        
        d_eng_10_90.push_back("Ten");
        d_eng_10_90.push_back("Twenty");
        d_eng_10_90.push_back("Thirty");
        d_eng_10_90.push_back("Forty");
        d_eng_10_90.push_back("Fifty");
        d_eng_10_90.push_back("Sixty");
        d_eng_10_90.push_back("Seventy");
        d_eng_10_90.push_back("Eighty");
        d_eng_10_90.push_back("Ninety");
        
        d_eng_100_end.push_back("");
        d_eng_100_end.push_back("Thousand");
        d_eng_100_end.push_back("Million");
        d_eng_100_end.push_back("Billion");
    }
    
    string numberToWords(int num) {
        
        int idx = 3;
        int base = 1000000000;
        string result;
        
        while (idx >= 0)
        {
            int curr = num / base;
            //cout << base << curr << endl;
            string currStr = convert3digit(curr);
            if (currStr.size() > 0) result += currStr + d_eng_100_end[idx] + " ";
            --idx;
            num %= base;
            base /= 1000;
        }
        
        if (result.empty()) return "Zero";
        
        while (!result.empty() && *result.rbegin() == ' ')
        {
            result.pop_back();
        }
        
        return result;
    }
    
    string convert3digit(int num)
    {
        string result;
        if (num == 0) return result;
        
        if (num / 100 != 0) result += d_eng_1_9[num / 100 - 1] + " " + "Hundred ";
        num %= 100;
        if (num == 0) return result;
        
        if (num < 10) result += d_eng_1_9[num - 1] + " ";
        else if (num > 10 && num < 20) result += d_eng_11_19[num % 10 - 1] + " ";
        else
        {
            result += d_eng_10_90[num / 10 - 1] + " ";
            num %= 10;
            if (num == 0) return result;
            result += d_eng_1_9[num - 1] + " ";
        }
        
        return result;
    }
private:
    vector<string> d_eng_1_9;
    vector<string> d_eng_11_19;
    vector<string> d_eng_10_90;
    vector<string> d_eng_100_end;
};