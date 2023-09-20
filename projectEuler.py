def multiplos35():
    numero_entero = int(input("Por favor, ingrese un número entero: "))
    sum=0
    for i in range(numero_entero):
        if i % 3 == 0 or i % 5 == 0:
            sum  = sum + i
        else:
            print("")
    return print(sum)

multiplos35()

'''#Funcion para calcular serie de fibonacci   
def fib(n):
    if n < 2:
        return n 
    else:
        return fib(n-1)+fib(n-2)

#Usando serie de fibonacci en un rango de 10

sum = 2
a = 1
b = 2
c = 0

while c <= 4000000:
    c = a + b
    if c%2 == 0:
        sum += c
    a,b = b,c
    print(a,b)'''
    
#Agregando nuevo comentario para segunda rama 

##otro comentario nadamas 
#otra cosa conflicto



    
    
    
    