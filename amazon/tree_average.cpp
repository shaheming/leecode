
// https://www.lintcode.com/problem/subtree-with-maximum-average/description

#include <vector>
#include <unordered_map>
#include <iostream>
#include <climits>
#include <string>
#include <queue>
using namespace std;

/**
 * Definition of TreeNode:
 * class TreeNode {
 * public:
 *     int val;
 *     TreeNode *left, *right;
 *     TreeNode(int val) {
 *         this->val = val;
 *         this->left = this->right = NULL;
 *     }
 * }
 */
#include <cfloat>
class Solution
{
private:
  double max_ave = -DBL_MAX;//注意
  TreeNode *max_node;

public:
  /**
     * @param root: the root of binary tree
     * @return: the root of the maximum average of subtree
     */

  TreeNode *findSubtree2(TreeNode *root)
  {
    // write your code here
    if (root == NULL)
      return NULL;
    pair<int, int> subtree;
    helper(root, &subtree);
    return max_node;
  }

  void helper(TreeNode *root, pair<int, int> *subtree)
  {
    if (root->left == NULL && root->right == NULL)
    {
      subtree->first = 1;
      subtree->second = root->val;
      if (subtree->second > max_ave)
      {
        max_ave = subtree->second;
        max_node = root;
      }//!!
      return;
    }
    int cnt = 0;
    double sum = 0;
    if (root->left)
    {
      pair<int, int> lSubtree;
      helper(root->left, &lSubtree);
      cnt += lSubtree.first;
      sum += lSubtree.second;
      if (sum / cnt > max_ave)
      {
        max_ave = sum / cnt;
        max_node = root->left;
      }
    }

    if (root->right)
    {
      pair<int, int> rSubtree;
      helper(root->right, &rSubtree);
      cnt += rSubtree.first;
      sum += rSubtree.second;
      if (sum / cnt > max_ave)
      {
        max_ave = sum / cnt;
        max_node = root->right;
      }
    }
    cnt++;
    sum += root->val;
    // cout << root->val << " " << sum / cnt << endl;
 

    subtree->first = cnt;
    subtree->second = sum;
  }
};