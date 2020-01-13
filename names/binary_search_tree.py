
class BinarySearchTree:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

    # Insert the given value into the tree
    def insert(self, value):
        if value < self.value:
            # if there is no left child
            if not self.left:
                self.left = BinarySearchTree(value)
            # if there is left child, recursion
            else:
                self.left.insert(value)
        else:
            # if there is no right child
            if not self.right:
                self.right = BinarySearchTree(value)
            # if there is right child, recursion
            else:
                self.right.insert(value)

    # Return True if the tree contains the value
    # False if it does not
    def contains(self, target):
        if self.value == target:
            return True

        if target < self.value and self.left:
            #if left child exist
            return self.left.contains(target)
          
        if target > self.value and self.right:
            #if right child does exist
            return self.right.contains(target)
           

        return False
    # Return the maximum value found in the tree
    def get_max(self):
        # max value is either self or from one of it's right children as left children are all smaller than self
        # SO ...  we are trying to find the MOST OUTTER RIGHT child in the tree
        
        #first, check for right child since right child will always be greater than self
        if self.right:
            return self.right.get_max()
        
        #if no right child, then self value is the greatest
        elif self:
            return self.value

        else:
            return None

    # Call the function `cb` on the value of each node
    # You may use a recursive or iterative approach
    def for_each(self, cb):
        cb(self.value)

        if self.left:
            self.left.for_each(cb)
        if self.right:
            self.right.for_each(cb)

    