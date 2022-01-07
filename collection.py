# You try to create a set of lists, but fail because lists are
# not hashable

# A set is a collection of elements like a list or a tuple. The
# collection consists of either primitive elements (integers,
# floats, strings), or complex elements (objects, tuples).
# However, all data types in a set must be hashable, meaning
# that they have an associated hash value.

hero = "Harry"
guide = "Dumbledore"
enemy = "Lord V."
print(hash(hero))
print(hash(guide))
print(hash(enemy))

## Can we create a set of strings?
characters = {hero, guide, enemy}
print(characters)