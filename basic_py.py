employees = {'Alice' : 100000,
             'Bob' : 99817,
             'Carol' : 122908,
             'Frank' : 88123,
             'Eve' : 93121}
top_earners = []
for key, val in employees.items():
    if val >= 100000:
        top_earners.append((key,val))
print(top_earners)


## Data
employees = {'Alice' : 100000,
             'Bob' : 99817,
             'Carol' : 122908,
             'Frank' : 88123,
             'Eve' : 93121}
## One-Liner
top_earners = [(k, v) for k, v in employees.items() if v >= 100000]
## Result
print(top_earners)
#expression and context example

print([x*2 for x in range (3)])

# Expression ➊: Create a new tuple from the context
# variables x and y.
# Context ➋: The context variable x iterates over all values
# returned by the range function (0, 1, 2), while context variable y
# iterates over all values returned by the range function (0, 1, 2).
print([(x, y) for x in range(3) for y in range(3)])

# Expression - Square function on the context variable x.
# Context ➋: Context variable x iterates over all values
# returned by the range function—0, 1, 2, 3, 4, 5, 6, 7, 8, 9—but
# only if they are odd values; that is, x % 2 > 0.

print([x ** 2 for x in range(10) if x % 2 > 0])


print([x.lower() for x in ['I', 'AM', 'NOT', 'SHOUTING']])
print([x.upper() for x in ['i', 'am', 'not', 'shooting']])

# expression - String lowercase function on context
# variable x.
# Context - Context variable x iterates over all string
# values in the list: 'I', 'AM', 'NOT', 'SHOUTING'


## Data
employees = {'Alice' : 100000,
             'Bob' : 99817,
             'Carol' : 122908,
             'Frank' : 88123,
             'Eve' : 93121}
## One-Liner
top_earners = [(k, v) for k, v in employees.items() if v >= 100000]
## Result
print(top_earners)
# Expression ➊: Creates a simple (key, value) tuple for
# context variables k and v.
# Context ➋: The dictionary method dict.items() ensures that
# context variable k iterates over all dictionary keys and that
# context variable v iterates over the associated values for
# context variable k—but only if the value of context variable v
# is larger than or equal to 100,000 as ensured by the
# if condition.
