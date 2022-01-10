# The dot regex matches any
# character (including whitespace characters). You can use it to
# indicate that you don’t care which character matches, as long
# as exactly one matches:

import re
text = '''A blockchain, originally block chain,
is a growing list of records, called blocks,
which are linked using cryptography.
'''
print(re.findall('b...k', text))
# ['block', 'block', 'block']