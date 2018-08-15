# Enter your code here. Read input from STDIN. Print output to STDOUT
'''
class Node:
      def __init__(self,info): 
          self.info = info  
          self.left = None  
          self.right = None 
           

       // this is a node of the tree , which contains info as data, left , right
'''
def height(root):
    depth = getDepth(root);
    return depth-1; 
   
    
    
def getDepth(root):
    if root is None:
        return 0;
    else:
        return (1+max(getDepth(root.left),getDepth(root.right)));
