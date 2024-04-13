var1 = 4
if (type(var1) != int):
    print("Erro, não é uma int")
else:
    print("Var é uma int =",var1)
    
var2 = "Hello World"
if (type(var2) != int):
    print("Erro, não é uma int")
else:
    print("Var é uma int =",var2)
    
def subtracao(a,b):
    try:
        resultado = a-b 
        print("Resultado é",resultado)
    except TypeError:
        print("Erro, tipo de variaveis invalidas")
        
subtracao(var1,var2)
var2 = 3 #Redefinindo para int
subtracao(var1,var2) #Resultado esperado nesse caso é resultado = 1