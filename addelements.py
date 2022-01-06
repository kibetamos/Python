# 1. Append
l = [1, 2, 2]
l.append(4)
print(l)

# 2. Insert
l = [1, 2, 4]
l.insert(2, 3)
print(l)

# 3. List Concatenation
print([1, 2, 2] + [4])

#the
# append operation is the fastest because it neither has to
# traverse the list to insert an element at the correct position (as
# with insert), nor create a new list out of two sublists (as with
# list concatenation)

# Removing Elements

l = [1, 2, 2, 4]
l.remove(1)
print(l)

# Reversing Lists
l = [1, 2, 2, 4]
l.reverse()
print(l)

# Sorting Lists
l = [2, 1, 4, 2]
l.sort()
print(l)