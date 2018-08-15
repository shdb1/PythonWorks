def postOrder(root):
    #Write your code here
    if root is not None:
        if root.left is not None:
            postOrder(root.left);
        if root.right is not None:
            postOrder(root.right);
        print(root.info, end=' ', flush=True);
            
    else:
        print('not a valid tree')
