class Solution {
public:
    int maxProfit(vector<int>& prices) {
        int l = 0;
        int r = 0;
        int max = 0;
        while (r < prices.size()) {
            int diff = prices.at(r) - prices.at(l);
            std::cout << diff << std::endl;
            if (diff > max) {
                max = diff;
            }
            else if (diff < 0) {
                l = r;
            }
            r++;
        }
        return max;
    }
};
