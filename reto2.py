#Condiciones anidadas ELIF 


mesDelAño=input("Digite el mes del año actual: ")

if mesDelAño=='Enero' or mesDelAño=='Febrero' or mesDelAño=='Marzo':  
    print(f'Estamos en invierno')
elif mesDelAño=='Abril' or mesDelAño=='Mayo' or mesDelAño=='Junio': 
    print(f'Estamos en Primavera')
elif mesDelAño=='Julio' or mesDelAño=='Agosto' or mesDelAño=='Septiembre':  
    print(f'Estamos en Verano')
elif mesDelAño=='Octubre' or mesDelAño=='Noviembre' or mesDelAño=='Diciembre':  
    print(f'Estamos en otoño')
else:
    print(f'El campo debe ser un mes')