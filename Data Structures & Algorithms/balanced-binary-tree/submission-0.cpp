/**
 * Definition for a binary tree node.
 * struct TreeNode {
 *     int val;
 *     TreeNode *left;
 *     TreeNode *right;
 *     TreeNode() : val(0), left(nullptr), right(nullptr) {}
 *     TreeNode(int x) : val(x), left(nullptr), right(nullptr) {}
 *     TreeNode(int x, TreeNode *left, TreeNode *right) : val(x), left(left), right(right) {}
 * };
 */

class Solution {
public:
    int maxDepth(TreeNode* root) {
        if (root == nullptr) {
            return 0;
        }
        int left = 1 + maxDepth(root->left);
        int right = 1 + maxDepth(root->right);
        if (left > right) {
            return left;
        } else {
            return right;
        }
    }
    bool isBalanced(TreeNode* root) {
        if (!root) {
            return true;
        }
        if (abs(maxDepth(root->left) - maxDepth(root->right)) > 1) {
            return false;
        }
        return (isBalanced(root->left) && isBalanced(root->right));
    }
};
