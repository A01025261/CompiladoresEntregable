#Autor: A01025261   Maximiliano Carrasco Rojas 


from delta import Compiler, Phase

source = """
var n, r, i;
n = 5;
r = 1;
i = 0;
do {
    i = i + 1;
    r = r * i;
} while n - i;
r
"""

c = Compiler('program')
c.realize(source, Phase.EVALUATION)
print("Parse Tree:")
print(c.parse_tree_str)

print("Symbol Table:")
print(c.symbol_table)

print("Generated WAT Code:")
print(c.wat_code)

print("Evaluation Result:")
print(c.result)