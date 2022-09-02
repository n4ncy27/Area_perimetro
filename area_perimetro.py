import math
#programa numero 1:area perimetro calculo.
print("-------------------")
print("--area_ perimetro:_")
print("-------------------")

# input
r=input("digite el valor del radio: ")
r=int (r)

# proccesing
A= math.pi*r*r
P=2*math.pi*r

#output
print("_________RESULTADO_______")
print ("el area es: "+ str(A))
print ("el perimetro es: "+ str(P))

