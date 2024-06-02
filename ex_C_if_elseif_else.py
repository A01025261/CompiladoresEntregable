#Autor: A01025261   Maximiliano Carrasco Rojas 


from delta import Compiler, Phase

source = """
var x, y;
x = 5;
if (x - 5) {
    y = 1;
} else if (x * 0) {
    y = 2;
} else if (x - 1) {
    y = 3;
} else {
    y = 4;
}
y
"""

c = Compiler('program')
c.realize(source, Phase.EVALUATION)
print(c.result)