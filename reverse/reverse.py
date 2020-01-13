class Node:
  def __init__(self, value=None, next_node=None):
    # the value at this linked list node
    self.value = value
    # reference to the next node in the list
    self.next_node = next_node

  def get_value(self):
    return self.value

  def get_next(self):
    return self.next_node

  def set_next(self, new_next):
    # set this node's next_node reference to the passed in node
    self.next_node = new_next

class LinkedList:
  def __init__(self):
    # reference to the head of the list
    self.head = None

  def add_to_head(self, value):
    node = Node(value)
    if self.head is not None:
      node.set_next(self.head)
    
    self.head = node

  def contains(self, value):
    if not self.head:
      return False
    # get a reference to the node we're currently at; update this as we traverse the list
    current = self.head
    # check to see if we're at a valid node 
    while current:
      # return True if the current value we're looking at matches our target value
      if current.get_value() == value:
        return True
      # update our current node to the current node's next node
      current = current.get_next()
    # if we've gotten here, then the target node isn't in our list
    return False




    
  def reverse_list(self):
    if self.head == None:
      return None

    if self.head.next_node == None:
      return self

    rev_list = LinkedList()
    rev_list.add_to_head(self.head.value)
    rev_list.head.next_node = None

    current = self.head

    while current.next_node:
      rev_list.add_to_head(current.next_node.value)
      current = current.next_node

    self.head = rev_list.head
   






    # # TO BE COMPLETED
    # rev_list = LinkedList()

    # #initializing the head node (which essentially will be the tail node)
    # rev_list.add_to_head(self.head) 

    # #setting head/tail node's next to None
    # rev_list.head.next_node = None 

    # current = self.head.next_node

    # while current:
    #   old_head = rev_list.head
    #   rev_list.add_to_head(current)
      
    #   rev_list.head.next_node = old_head
    #   current = current.next_node

    # return rev_list

    # current = self.head  # self.head is going to be the tail
    # next_node = current.next
    # while current:
    #   rev_list.add_to_head(current)
    #   current = next_node
    #   next_node = next_node.next