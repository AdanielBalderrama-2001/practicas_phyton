from re import I


num_tabla = int (input("Ingrese un numero para ver su tabla de multiplicar :"))
print(f"--- Tabla del {num_tabla}--- ")
for i in range (1,11):
        resultado = num_tabla * i
        print(f"{num_tabla} x {i} = {resultado}")
        