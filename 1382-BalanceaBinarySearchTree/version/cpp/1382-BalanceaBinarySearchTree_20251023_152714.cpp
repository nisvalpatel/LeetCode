// Last updated: 10/23/2025, 3:27:14 PM
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
    // Get height of a node
    int height(TreeNode* node) {
        if (!node) return 0;
        return 1 + max(height(node->left), height(node->right));
    }

    // Get balance factor of a node
    int getBalance(TreeNode* node) {
        if (!node) return 0;
        return height(node->left) - height(node->right);
    }

    // Right rotation
    TreeNode* rightRotate(TreeNode* y) {
        TreeNode* x = y->left;
        TreeNode* T2 = x->right;

        // Perform rotation
        x->right = y;
        y->left = T2;

        // Return new root
        return x;
    }

    // Left rotation
    TreeNode* leftRotate(TreeNode* y) {
        TreeNode* x = y->right;
        TreeNode* T2 = x->left;

        // Perform rotation
        x->left = y;
        y->right = T2;

        return x;
    }

    // Insert node into AVL tree
    TreeNode* insert(TreeNode* root, int key) {
        // 1️⃣ Standard BST insert
        if (!root) return new TreeNode(key);

        if (key < root->val)
            root->left = insert(root->left, key);
        else if (key > root->val)
            root->right = insert(root->right, key);
        else
            return root; // no duplicates

        // 2️⃣ Get balance factor
        int balance = getBalance(root);

        // 3️⃣ Perform rotations if unbalanced

        // Left Left Case
        if (balance > 1 && key < root->left->val)
            return rightRotate(root);

        // Right Right Case
        if (balance < -1 && key > root->right->val)
            return leftRotate(root);

        // Left Right Case
        if (balance > 1 && key > root->left->val) {
            root->left = leftRotate(root->left);
            return rightRotate(root);
        }

        // Right Left Case
        if (balance < -1 && key < root->right->val) {
            root->right = rightRotate(root->right);
            return leftRotate(root);
        }

        return root; // return balanced root
    }

    // Inorder traversal to get sorted values
    void inorder(TreeNode* root, vector<int>& vals) {
        if (!root) return;
        inorder(root->left, vals);
        vals.push_back(root->val);
        inorder(root->right, vals);
    }

    // Build balanced BST using AVL insertion
    TreeNode* balanceBST(TreeNode* root) {
        vector<int> vals;
        inorder(root, vals); // get sorted list of all nodes
        TreeNode* newRoot = nullptr;
        for (int v : vals)
            newRoot = insert(newRoot, v); // insert each into AVL tree
        return newRoot;
    }
};
