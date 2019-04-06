def preorderTraversal(self,root):
  r = []
  if root is None:
    return r
  
  stack = [root]
  while stack:
    tmp = stack.pop()
    r.append(tmp.val)
    if tmp.right:
      stack.append(tmp.right)
    if tmp.left:
      stack.append(tmp.left)
    
  return r


def inorderTraversal(self,root):
  r = []
  if root is None:
    return r
  p = root
  while p is not None or stack:
    while p is not None:
      stack.append(p)
      p = p.left
    p = stack.pop()
    r.append(p.val)
    p = p.right
  return r