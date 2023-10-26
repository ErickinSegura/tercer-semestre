#Factorial Recursivo
#Erick Segura Sanchez

def factorial(n):
    if n <= 0:
        return 1
    
    else:
        return n * factorial(n-1)

n=int(input("Escribe el numero que necesitas el factorial: "))
print(f'{n}! es igual a {factorial(n)}')