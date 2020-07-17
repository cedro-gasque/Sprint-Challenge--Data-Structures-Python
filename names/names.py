import time
from binary_search_tree import BSTNode
start_time = time.time()
hash = lambda s : sum([ord(c) for c in s])
with open('names_1.txt', 'r') as f:
    names_1 = f.read().split("\n")  # List containing 10000 names
    bst = BSTNode(names_1[0])
    for i in range(1, len(names_1)):
        bst.insert(names_1[i])

duplicates = []  # Return the list of duplicates in this data structure

with open('names_2.txt', 'r') as f:
    names_2 = f.read().split("\n")  # List containing 10000 names
    for n in names_2:
        bst.contains(n) and duplicates.append(n)
end_time = time.time()
print (f"{len(duplicates)} duplicates:\n\n{', '.join(duplicates)}\n\n")
print (f"runtime: {end_time - start_time} seconds")

# ---------- Stretch Goal -----------
# Python has built-in tools that allow for a very efficient approach to this problem
# What's the best time you can accomplish?  Thare are no restrictions on techniques or data
# structures, but you may not import any additional libraries that you did not write yourself.
