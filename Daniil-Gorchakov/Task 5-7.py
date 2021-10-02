### Task 4.7*
'''
Run the module `modules/mod_a.py`. Check its result. Explain why does this
happen.
Try to change x to a list `[1,2,3]`. Explain the result.
Try to change import to `from x import *` where x - module names. Explain the
result. 
'''

import sys
sys.path.append("modified modules")

import mod_a
import mod_b
import mod_c
"""return 6
mod_c.py
x = 5

mod_b.py -> import mod_c
mod_c.x = 6 #overwrite variable x

mod_a.py -> import mod_b -> import mod_c
print(mod_c.x)
"""

import mod_a_1
"""return mod_c_1.x
mod_c_1.py
x = [1, 2, 3]

mod_b_1.py -> import mod_c_1
mod_c_1.x = "mod_c_1.x" #overwrite variable x

mod_a_1.py -> import mod_b_1 -> import mod_c_1
print(mod_c_1.x)
"""

from  mod_a_2 import *
"""return mod_c_2.x
mod_c_2.py
x = [1, 2, 3, 4]

mod_b_2.py -> import mod_c_2
mod_c_2.x = "mod_c_2.x" #overwrite variable x

mod_a_2.py -> import mod_b_2 -> import mod_c_2
print(mod_c_2.x)
"""
