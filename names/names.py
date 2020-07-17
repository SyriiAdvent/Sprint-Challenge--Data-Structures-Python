import os
import time
from binary_search_tree import BSTNode as BST
import threading

start_time = time.time()
dirpath = os.path.dirname(os.path.abspath(__file__))

f = open(dirpath + '/names_1.txt', 'r')
names_1 = f.read().split("\n")  # List containing 10000 names
f.close()

f = open(dirpath + '/names_2.txt', 'r')
names_2 = f.read().split("\n")  # List containing 10000 names
f.close()

t_name_1 = threading.Thread(target=names_1)
t_name_2 = threading.Thread(target=names_2)


# sorted_names_2 = sorted(names_2, key=len)

duplicates = []  # Return the list of duplicates in this data structure

# Replace the nested for loops below with your improvements
def linear_search(lst, lst2):
    for name_1 in names_1:
        for name_2 in names_2:
            if name_1 == name_2:
                duplicates.append(name_1)

# My systems time average is runtime: 1.6299986839294434 seconds (64 Dupes)
# linear_search(names_1, names_2)


# Improved version
def binary_search(lst, lst2):
  bst = BST(names_1[0])
  for i in range(len(names_1)):
      if i != 0:
          bst.insert(names_1[i])
  for name_2 in names_2:
      if bst.contains(name_2):
          duplicates.append(name_2)

# My systems new time average is runtime: 0.06849813461303711 seconds (64 Dupes)
binary_search(names_1, names_2)


end_time = time.time()
print (f"Found: {len(duplicates)} duplicates.")
# print (f"{len(duplicates)} duplicates:\n\n{', '.join(duplicates)}\n\n") # too spammy!
print (f"runtime: {end_time - start_time} seconds")

# ---------- Stretch Goal -----------
# Python has built-in tools that allow for a very efficient approach to this problem
# What's the best time you can accomplish?  Thare are no restrictions on techniques or data
# structures, but you may not import any additional libraries that you did not write yourself.


# Super easy one :D !!!

# duplicates = set(names_1).intersection(names_2)