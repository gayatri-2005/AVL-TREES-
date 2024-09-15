class AVLwithParent:
    def _init_(self):
        # Pointer to the left and the right subtree
        self.left = None
        self.right = None

        # Stores the data in the node
        self.key = None

        # Stores the parent pointer
        self.par = None

        # Stores the height of the current tree
        self.height = None
