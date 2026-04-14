class Solution {
public:
    bool isPalindrome(string s) {
        s.erase(std::remove_if(s.begin(), s.end(), 
        []( auto const& c ) -> bool { return !std::isalnum(c); } ), s.end());
        bool out = true;
        for (int i = 0; i < s.length(); i++) {
            s[i] = tolower(s[i]);
        }
        for (int i = 0; i < s.length() / 2; i++) {
            std::cout << s[s.length() - i - 1] << std::endl;
            if (s[i] != s[s.length() - i - 1]) {
                out = false;
            }
        }
        return out;
    }
};
