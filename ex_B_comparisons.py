#Autor: A01025261   Maximiliano Carrasco Rojas 


from delta import Compiler, Phase

source = '1 <= 2 == 1 != 0 > 0 < 0 <= 1'

c = Compiler('program')
c.realize(source, Phase.EVALUATION)
# print(c.parse_tree_str)
# print(c.wat_code)
print(c.result)