# The map() function adds a Boolean value to each string element
# in the original txt list. This Boolean value is True if the string
# element contains the word anonymous. The first argument is
# the anonymous lambda function, and the second is a list of
# strings you want to check for the desired string.
## Data
txt = ['lambda functions are anonymous functions.',
       'anonymous functions dont have a name.',
       'functions are objects in Python.']
## One-Liner
mark = map(lambda s: (True, s) if 'anonymous' in s else (False, s), txt)
## Result
print(list(mark))