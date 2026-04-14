class Solution {
public:
    bool isValid(string s) {
        std::stack<char> stack;
        bool out = true;
        for (char c : s) {
            if (c == '(' || c == '{' || c == '[') {
                stack.push(c);
            } else if (stack.empty()) {
                out = false;
            }
            else if (stack.top() == '(' && c == ')' || stack.top() == '{' && c == '}' || stack.top() == '[' && c == ']') {
                stack.pop();
            } else {
                out = false;
            }
        }
        if (!stack.empty()) {
            out = false;
        }
        return out;
    }
};
