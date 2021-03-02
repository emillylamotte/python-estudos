#Algoritmo que calcula raizes de uma equação de segundo grau
#Emilly Lamotte

a = float (input ("Digite o coeficiente de x^2:"))
b = float (input ("Digite o coeficiente de x:"))
c = float (input ("Digite o termo independente:"))

delta = b**2 - (4*a*c)

if delta >= 0:
    
    print ("Delta igual a:")
    print (delta)
    import math 
    raiz = math.sqrt(delta)
    x1 = ((-b) + raiz)/(2*a)
    x2 = ((-b) - raiz)/(2*a)
    print ("x1 igual a:")
    print (x1)
    print ("x2 igual a:")
    print (x2)

else:
    
    print ("Delta invalido, nao existem raizes reais")
 
