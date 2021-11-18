# def nodeDepth(root):
#     sumOfDepths = 0
#     stack=[{'node': root, 'depth': 0}]
#     while len(stack) > 0:
#         nodeInfo = stack.pop()                                                    #iteration method
#         node, depth = nodeInfo['node'], nodeInfo['depth']
#         if node is none:
#             continue
#         sumOfDepths += depth
#         stack.append({'node': root.left, 'depth': depth + 1})
#         stack.append({'node': root.right, 'depth': depth + 1})
#     return sumOfDepths


# def nodeDepth(root, sum=0):
#     if not root:
#         return 0
#     return sum + nodeDepth(root.left, sum + 1) + nodeDepth(root.right, sum+1)     #recursive method


# class BinaryTree:
#     def __init__(self, value):
#         self.value = value
#         self.left = None
#         self.right = None
