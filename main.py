def func(x):
    x += 5
    return x # permitir o uso da função diretamente

x = 3
var = x + func(x)
print(var)


x = 3
var = func(x) + x
print(var)
