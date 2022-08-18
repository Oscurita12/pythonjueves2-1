#Multiplo de 3

numero = int(input("Digite un número entero: "))
modulo = numero % 3
print(f'El modulo del número es: {modulo}')


#Condiciones en Python 
#if()
if modulo==0:    
    print(f'El número {numero} es multiplo de 3')
else:   
    print(f'El número {numero} NO es multiplo de 3')

print("fin del progrma")