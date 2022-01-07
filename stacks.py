# The stack data structure works intuitively as a first-in, first-out
# (FIFO) structure.
# Think of it as a stack of paperwork: you
# place every new paper on the top of a pile of old papers, and
# when you work through the stack, you keep removing the
# topmost document.
stack = [3]
stack.append(42) # [3, 42]
stack.pop() # 42 (stack: [3])
stack.pop() # 3 (stack: [])
