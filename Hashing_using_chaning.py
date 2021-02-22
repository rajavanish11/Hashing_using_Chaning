class Node:

  def __init__(self,key,value):

    self.key = key
    self.value = value
    self.next = None

###########################################
#linkedlist class
class LL:

  def __init__(self):

    self.head = None

  def add(self,key,value):

    new_node = Node(key,value)

    if self.head is None:
      self.head = new_node
    else:
      temp = self.head

      while temp.next is not None:
        temp = temp.next

      temp.next = new_node

  def remove_head(self):

    if self.head is None:
      return -1
    else:
      self.head = self.head.next
      return 1

  
  def remove(self,key):

    if self.head.key == key:
      return self.remove_head()

    temp = self.head

    while temp.next is not None:

      if temp.next.key == key:
        break

      temp = temp.next

    if temp.next is None:
      return -1
    else:
      temp.next = temp.next.next
      return 1
    

  def traverse(self):

    temp = self.head

    while temp is not None:
      print(temp.key, "-->", temp.value,"   ", end=" ")
      temp = temp.next

  def size(self):

    temp = self.head
    counter = 0

    while temp is not None:
      temp = temp.next
      counter+=1

    return counter

  def get_node(self, index):

    temp = self.head
    counter = 0

    while temp is not None:

      if counter == index:
        return temp
      
      temp = temp.next
      counter+=1

  def search(self,key):

    temp = self.head
    pos = 0

    while temp is not None:

      if temp.key == key:
        return pos

      pos+=1
      temp = temp.next
    
    return -1



#####################################
class Dictionary:

  def __init__(self, capacity):

    self.capacity = capacity
    self.buckets = self.init_array(self.capacity)
    self.size = 0

  def init_array(self,capacity):
    L = []

    for i in range(capacity):
      L.append(LL())

    return L

  def __setitem__(self,key,value):
    self.put(key,value)

  def put(self,key,value):

    # calculate hash value
    bucket_index = self.hash_function(key)

    item_index = self.get_item_index(bucket_index,key)

    if item_index == -1:
      # insert
      self.buckets[bucket_index].add(key,value)
      self.size+=1
      load_factor = self.size/self.capacity
      print("load factor = ",self.size/self.capacity)

      if load_factor >= 2:
        self.rehash()
      # load factor
    else:
      # update
      node = self.buckets[bucket_index].get_node(item_index)
      node.value = value

  def rehash(self):

    # copy existing buckets into a variable
    old_buckets = self.buckets
    # create a new array with double capacity
    self.buckets = self.init_array(2 * self.capacity)
    # reset capacity
    self.capacity = self.capacity * 2
    # set size = 0
    self.size = 0
    # run through all the older nodes and rehash

    for i in old_buckets:
      for j in range(i.size()):
        node = i.get_node(j)
        node_key = node.key
        node_value = node.value
        self.put(node_key,node_value)

  def get(self,key):

    bucket_index = self.hash_function(key)

    item_index = self.buckets[bucket_index].search(key)

    if item_index == -1:
      return "Not Present"
    else:
      node = self.buckets[bucket_index].get_node(item_index)
      return node.value

  def __getitem__(self,key):
    return self.get(key)

  def __len__(self):
    return self.size

  def __delitem__(self,key):
    bucket_index = self.hash_function(key)

    res = self.buckets[bucket_index].remove(key)
    if res == -1:
      return "Not Present"

  def __str__(self):
    for i in self.buckets:
      i.traverse()

    return ""

  def get_item_index(self,bucket_index,key):

    item_index = self.buckets[bucket_index].search(key)

    return item_index

  def hash_function(self, key):
    return abs(hash(key)) % self.capacity





#####
#1.create dist usnig Dictionary funtion ,passing array size.
# eg-D1 = Dictionary(4)

#2.put item in dict usnig put funtion
#eg-
#D1.put("java",100)
#D1.put("python",200)
#D1.put("c",300)
#D1.put("ruby",400)
#D1.put("c++",500)
#3.print dict
#eg-print(D1)

####output will be
##  java --> 100     c++ --> 500     c --> 300     python --> 200     ruby --> 400
