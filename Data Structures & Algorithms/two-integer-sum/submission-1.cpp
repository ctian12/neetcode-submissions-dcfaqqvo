class Solution {
public:
    vector<int> twoSum(vector<int>& nums, int target) {
        unordered_map<int, int> need; 
        for (int i = 0; i < nums.size(); i++) {
            int diff = target - nums[i];
            if (need.find(diff) != need.end()) {
                return {need[diff], i};
            }
            need.insert({nums[i], i});
        }
        return {};
    }
};