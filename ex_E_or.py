# Autor: A01025261 Maximiliano Carrasco Rojas

from delta import Compiler, Phase

source = '10 || 20 || 30'

c = Compiler('program')
c.realize(source, Phase.EVALUATION)

# Debug prints
print("Parse Tree:")
print(c.parse_tree_str)

print("Symbol Table:")
print(c.symbol_table)

print("Generated WAT Code:")
print(c.wat_code)

print("Evaluation Result:")
print(c.result)
