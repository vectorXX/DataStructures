# BinarySearchTree: A binary search tree.

class BinarySearchTree:

    def __init__(self, key=None, left=None, right=None, parent=None):
        #self.data_tree = bst
        self.left = left
        self.right = right
        self.key = key
        self.parent = parent

    def insert(self, child):

        if child.key <= self.key:
            if self.left is None:
                self.left = child
                child.parent = self

            else:
                self.left.insert(child)

        elif child.key > self.key:
            if self.right is None:
                self.right = child
                child.parent = self

            else:
                self.right.insert(child)

    def search(self, value):
        if self:
            if self.key == value:
                return self
            elif value < self.key:
                return None if self.left is None else self.left.search(value)
            elif value > self.key:
                return None if self.right is None else self.right.search(value)
            else:
                return self

    def delete(self, key):
        """ delete the node with the given key and return the
        root node of the tree """

        if self.key == key:
            # delete function is called recursively (see matching else) until we have the node we want to delete

            if self.right and self.left:   #both children present

                new_replacement = self.right.minimum()

                # here the replacement node is direct child of to be deleted node (replacement has no left child, so is already minimum)
                if new_replacement.parent.right == new_replacement:
                    new_replacement.parent.right = new_replacement.right

                # here the replacement node is the minimum of the right branch of to be deleted node
                else:
                    #note: new_replacement has no left child, since is minimum, but may have a right child
                    # the new_replacement.parent is NOT the to be deleted node, just the node above minimum
                    # new_replacement spot will be taken by its right child
                    new_replacement.parent.left = new_replacement.right

                # reset the left and right children of the successor

                new_replacement.left = self.left
                new_replacement.right = self.right
                return new_replacement

            else: #only one child present, or no child present
                # "easier" case
                # if self.left:
                #     return self.left  # promote the left subtree
                # else:
                #     return self.right  # promote the right subtree
                if self.right:
                    return self.right  # promote the right subtree, right takes precedence
                elif self.left:
                    return self.left  # promote the left subtree
                else:
                    return None #deleted the root node, with no children
        else:
            if self.key > key:  # key should be in the left subtree
                if self.left:
                    self.left = self.left.delete(key) # recursively call delete, with left child node
                # else the key is not in the tree, will return self below

            else:  # key should be in the right subtree
                if self.right:
                    self.right = self.right.delete(key) # recursively call delete, with right child node
                # else the key is not in the tree, will return self below
        return self

    def is_leaf(self):
        return self.left is None and self.right is None

    def has_left_child(self):
        return self.left is not None

    def has_right_child(self):
        return self.left is not None

    def minimum(self):
        itr = self
        while itr.left:
            itr = itr.left
        return itr
