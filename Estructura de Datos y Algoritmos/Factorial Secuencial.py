#Factorial Secuencial
#Erick Segura Sanchez

def factorial(n):
    if n == 0:
        return 1
    elif n<0:
        return "No existe el factorial de un numero negativo"
    else:
        fact=1
        for i in range(1,n+1):
            fact=fact*i
        return fact

n=int(input("Escribe el numero que necesitas el factorial: "))
print(f'{n}! es igual a {factorial(n)}')
