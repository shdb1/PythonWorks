def inOrder(root):
    #Write your code here
    if root is not None:
        if root.left is not None:
            inOrder(root.left);
        print(root.info, end=' ', flush=True);
        if root.right is not None:
            inOrder(root.right);
        
            
    else:
        print('not a valid tree')
