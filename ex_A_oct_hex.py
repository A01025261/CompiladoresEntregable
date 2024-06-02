#Autor: A01025261   Maximiliano Carrasco Rojas 

# File: ex_A_oct_hex.py

from delta import Compiler, Phase

source = '#b1010'

c = Compiler('program')
c.realize(source, Phase.EVALUATION)
# print(c.parse_tree_str)
# print(c.wat_code)
print(c.result)