import numpy as np
h=0
k=0
#utilice el for para poder probar el codigo y revisar que funcionara con pocos estudiantes y saber que sirve para 6500 o más 
x=int(input("ingrese la cantidad de estudiantes (para hacer la prueba con 6500 estudiantes escribir 6500)\n"))
for i in range (1,x+1):
    a=int(input(f"ingrese el codigo del estudiante: {i}\n"))
    b=input(f"ingrese el nombre del estudiante: {i}\n")
    c=float(input(f"ingrese el promedio acumulado del estudiante: {i}\n"))
    d=input(f"ingrese la carrera del estudiante: {i}\n")
    e=int(input(f"ingrese el año de ingreso del estudiante: {i}\n"))
    L=np.array([a,b,c,d,e])
    if c>=4:
        print("El siguiente estudiante tiene un promedio mayor o igual a 4\n")
        print(f"Codigo: {(L[0])}, - Nombre: {(L[1])}, - Carrera: {(L[3])}") 
        h=h+1
    if e<1990:
        k=k+1
        if 2.8<=c<=3.2:
            print("El siguiente estudiante ingreso antes de 1990 y esta condicional\n")
            print(f"Codigo: {(L[0])}, - Nombre: {(L[1])}")

print(f"la cantidad de estudiantes que sacaron un promedio igual o mayor a 4 fueron: {h}")
print(f"la cantidad de estudiantes que ingresaron antes de 1990 son: {k}")