
# The zero-or-one regex, ?, applies to the regex immediately
# in front of it. In our case, this is the character s.
# The zero-orone regex says that the pattern it modifies is optional
import re
text = '''A blockchain, originally block chain,
is a growing list of records, called blocks,
which are linked using cryptography.
'''

print(re.findall('blocks?', text))
# ['block', 'block', 'blocks']
