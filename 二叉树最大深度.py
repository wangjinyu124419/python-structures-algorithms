class Node():
    def __init__(self,item=None):
        self.item=item
        self.lchild=None
        self.rchild=None
    def __str__(self):
        return str(self.item)

class Tree():
    def __init__(self,root=None):
        self.root=root
        self.max_depth=0
    #添加节点
    def add(self, elem):
        """为树添加节点"""
        node = Node(elem)
        #如果树是空的，则对根节点赋值
        if self.root == None:
            self.root = node
        else:
            queue = []
            queue.append(self.root)
            #对已有的节点进行层次遍历
            while queue:
                #弹出队列的第一个元素
                cur = queue.pop(0)
                if cur.lchild == None:
                    cur.lchild = node
                    return
                elif cur.rchild == None:
                    cur.rchild = node
                    return
                else:
                    #如果左右子树都不为空，加入队列继续判断
                    queue.append(cur.lchild)
                    queue.append(cur.rchild)


    def preorder(self,root):
        if not root:
            return
        print(root.item)
        self.preorder(root.lchild)
        self.preorder(root.rchild)

    def inorder(self, root):
        if not root:
            return
        self.inorder(root.lchild)
        print(root.item)
        self.inorder(root.rchild)

    def postorder(self,root):
        if not root:
            return

        self.postorder(root.lchild)
        self.postorder(root.rchild)
        print(root.item)

    def get_max_depth(self,root,depth=0,):
        if not root:
            if depth>self.max_depth:
                self.max_depth=depth
        self.get_max_depth(root.lchild,depth=depth+1)
        self.get_max_depth(root.rchild,depth=depth+1)
        return self.max_depth




