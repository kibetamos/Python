# The asterisk operator applies to the regex immediately in
# front of it. In this example, the regex pattern starts with the
# character 'y', followed by an arbitrary number of characters, .*,
# followed by the character 'y'. As you can see, the word
# 'cryptography' contains one such instance of this pattern:
# 'yptography'.

import re
text = '''A blockchain, originally block chain,
is a growing list of records, called blocks,
which are linked using cryptography.
'''

print(re.findall('y.*y', text))
# ['yptography']
