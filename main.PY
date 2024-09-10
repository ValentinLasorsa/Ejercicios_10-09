import os
#EJ 1
"""
print("Ejercicio 1")
suma=0
num=int(input("Ingrese un número "))
while num>=0:
    suma=suma+num
    num=int(input("Ingrese otro número "))
print("Terminó el ciclo! la suma fue de:",suma)
input("\033[1mPresione enter para continuar\033[0m")
os.system('cls')

#EJ 2
print("Ejercicio 2")
sumaNotas=0
cantAlumnos=0
nota=int(input("Ingrese la nota  "))
while nota>=0:
    sumaNotas=sumaNotas+nota
    cantAlumnos=cantAlumnos+1
    nota=int(input("Ingrese la próxima nota "))
promNota=sumaNotas/cantAlumnos
print("El promedio de notas fue de:",promNota)
input("\033[1mPresione enter para continuar\033[0m")
os.system('cls')

#EJ 3
print("Ejercicio 3")
input("\033[1mPresione enter para comenzar\033[0m")
i=1
while i <=100:
    print(i)
    i=i+1
input("\033[1mPresione enter para continuar\033[0m")
os.system('cls')

#EJ 4
print("Ejercicio 4")
sumaSueldo=0
cantSueldos=0
sueldo=float(input("Ingrese un sueldo "))
while sueldo !=0:
    sumaSueldo=sumaSueldo+sueldo
    cantSueldos=+= 1 
    sueldo=float(input("Ingrese otro sueldo "))
promSueldo=sumaSueldo/cantSueldos
print("Ciclo terminado! el promedio de sueldo fue de:",promSueldo)
input("\033[1mPresione enter para continuar\033[0m")
os.system('cls')

#EJ 5
print("Ejercicio 5")
numero=int(input("Ingrese un número "))
while numero!=0:
    if numero>0:
        print("El número ingresado fue positivo")
    else: 
        print("El número ingresado fue negativo")
    numero=int(input("Ingrese otro número "))
print("Ciclo terminado")
input("\033[1mPresione enter para continuar\033[0m")
os.system('cls')

#EJ 6
print("Ejercicio 6")
numMax=0
nums=int(input("Ingrese un número "))
while nums>=0:
    if nums >numMax:
        numMax=nums
    nums=int(input("Ingrese otro número "))
print("Ciclo terminado")
print("El valor máximo ingresado fue",numMax)
input("\033[1mPresione enter para continuar\033[0m")
os.system('cls')

#EJ 7
print("Ejercicio 7")
cantTemps=0
sumaTemps=0
cant0Grados=0
temperatura=int(input("Ingrese la temperatura en celsius "))
while temperatura<=50:
    cantTemps+= 1 
    sumaTemps=sumaTemps+temperatura
    if temperatura==0:
        cant0Grados = cant0Grados+1
    temperatura=int(input("Ingrese otra temperatura en celsius "))
promTemp=sumaTemps/cantTemps
print("La cantidad de temperatura de 0 grados fue de:",cant0Grados)
print("El promedio de temperaturas fue de:",promTemp)
input("\033[1mPresione enter para continuar\033[0m")
os.system('cls')

#EJ 8
print("Ejercicio 8")
sumaPares=0
num1=int(input("Ingrese un número "))
while num1 !=0:
    if num1 %2==0:
        sumaPares=sumaPares+num1
    num1=int(input("Ingrese otro número "))
print("Ciclo terminado!")
print("La suma de los pares fue de:",sumaPares)
input("\033[1mPresione enter para continuar\033[0m")
os.system('cls')

#EJ 9
print("Ejercicio 9")
sumas=0
num2=int(input("Ingrese un número "))
for k in range(num2):
    sumas=sumas+k
print("La suma de los números anteriores es de:",sumas)
input("\033[1mPresione enter para continuar\033[0m")
os.system('cls')

#EJ 10
print("Ejercicio 10")
cantNums=0
sumaNums=0
numy=int(input("Ingrese un número "))
while numy % 2 == 0 and numy >= 20:
    cantNums += 1 
    sumaNums += numy  
    numy = int(input("Ingrese otro número: "))
print("Ciclo terminado!")
if cantNums > 0:
    promNums = sumaNums / cantNums
    print("El promedio fue de:", promNums)
else:
    print("No se ingresaron números válidos para calcular el promedio.")
input("\033[1mPresione enter para continuar\033[0m")
os.system('cls')
"""
#EJ 11
print("Ejercicio 11")
turnoMañ=0
turnoTar=0
turnoNoc=0
cantTotal=0
sumaEdades=0
turno=int(input("Ingrese el turno del alumno "))
edad=int(input("Ingrese la edad del alumno "))
while turno !=0:
    sumaEdades=sumaEdades+edad
    cantTotal+= 1 
    if turno ==1:
        turnoMañ+= 1 
    elif turno ==2:
        turnoTar+= 1 
    elif turno ==3:
        turnoNoc+= 1 
    turno=int(input("Ingrese el turno del alumno "))
    edad=int(input("Ingrese la edad del alumno "))
print("Ciclo terminado!")
promEdades=sumaEdades/cantTotal
print("Cantidad total de alumnos:",cantTotal)
print("Cantidad de alumnos del turno mañana:",turnoMañ,"Cantidad de alumnos del turno tarde:",turnoTar,"Cantidad de alumnos del turno noche:",turnoNoc)
print("Promedio de edad:",promEdades)
input("\033[1mPresione enter para continuar\033[0m")
os.system('cls')