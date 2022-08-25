#Ejercicio de edad según el gobierno

edad=int(input("Digite su edad: "))

if edad>=0 and edad<14:    
    print(f'Niño')
elif edad>= 15 and edad<28: 
    print(f'Joven')
elif edad>=28 and edad<60:  
    print(f'Adulto')
elif edad>60:   
    print(f'Adulto mayor')
else:
    print(f'El campo no es válido')