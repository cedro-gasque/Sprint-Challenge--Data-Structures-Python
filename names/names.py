import time
from binary_search_tree import BSTNode
print("Binary Search Tree")
start_time = time.time()
duplicates = []
with open('names_1.txt', 'r') as f:
    with open('names_2.txt', 'r') as g:
        names_1 = f.read().split("\n")  # List containing 10000 names
        bst = BSTNode(names_1[0])
        for i in range(1, len(names_1)):
            bst.insert(names_1[i])
        for n in g.read().split("\n"):
            bst.contains(n) and duplicates.append(n)
end_time = time.time()
print (f"{len(duplicates)} duplicates:\n\n{', '.join(duplicates)}\n\n")
print (f"runtime: {end_time - start_time} seconds")

# ---------- Stretch Goal -----------
# Python has built-in tools that allow for a very efficient approach to this problem
# What's the best time you can accomplish?  Thare are no restrictions on techniques or data
# structures, but you may not import any additional libraries that you did not write yourself.
print("Sets")
start_time = time.time()
with open('names_1.txt', 'r') as f:
    with open('names_2.txt', 'r') as g:
        duplicates = set(f.read().split("\n")).intersection(set(g.read().split("\n")))
end_time = time.time()
print (f"{len(duplicates)} duplicates:\n\n{', '.join(duplicates)}\n\n")
print (f"runtime: {end_time - start_time} seconds")

# list version for stretch goal
print("fake DaC algorithm")
start_time = time.time()
with open('names_1.txt', 'r') as f:
    names_1 = f.read().split("\n")  # List containing 10000 names
with open('names_2.txt', 'r') as f:
    names_2 = f.read().split("\n")  # List containing 10000 names
def divide_and_conquer(value):
    global names_2
    l = len(value)
    return value * (value[0] in names_2) if l <= 1 else (
    divide_and_conquer(value[0:l//2]) + divide_and_conquer(value[l//2:l]))
duplicates = divide_and_conquer(names_1)
end_time = time.time()
print (f"{len(duplicates)} duplicates:\n\n{', '.join(duplicates)}\n\n")
print (f"runtime: {end_time - start_time} seconds")
