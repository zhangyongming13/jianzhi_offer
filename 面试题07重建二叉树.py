# https://leetcode-cn.com/problems/zhong-jian-er-cha-shu-lcof/
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


# 递归重构二叉树
# 前序遍历的首个元素即为根节点 root 的值；
# 在中序遍历中搜索根节点 root 的索引 ，可将中序遍历划分为 [ 左子树 | 根节点 | 右子树 ] 。
# 根据中序遍历中的左（右）子树的节点数量，可将前序遍历划分为 [ 根节点 | 左子树 | 右子树 ] 。
class Solution:
    def buildTree(self, preorder, inorder):
        if not preorder:
            return None
        # 先序遍历的第一个就是树的根（这里不一定是整个树的根，有可能是子树的根或者叶子）
        root_index = inorder.index(preorder[0])
        root = TreeNode(preorder[0])
        # 左右子节点进行递归操作
        root.left = self.buildTree(preorder[1: root_index + 1], inorder[:root_index + 1])
        root.right = self.buildTree(preorder[root_index + 1:], inorder[root_index + 1:])
        return root
