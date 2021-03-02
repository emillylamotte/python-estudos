#Algoritmo que realiza calculos basicos
#Emilly Lamotte

n1 = float (input("Digite o primeiro numero:"))
operador = input ("Digite a operacao desejada:")
n2 = float (input("Digite o segundo numero:"))

if operador == '+':
    
    resultado = n1 + n2

if operador == '-':
    
    resultado = n1 - n2

if operador == '*':
    
    resultado = n1 * n2
    
if operador == '/':
    
    resultado = n1/n2
    
if operador == '**':
    
    resultado = n1**n2
    
print ("O resultado da operacao eh:")
print (resultado)
