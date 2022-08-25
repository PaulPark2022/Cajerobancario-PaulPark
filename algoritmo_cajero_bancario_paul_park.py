# CajeroBancarioPaulPark

saldo = 5000

#Definicion de la funcion de ingreso
def monto_ingreso(suma):
  ingreso = saldo + suma
  return ingreso

#Definicion de la funcion de retiro
def monto_retiro(resta):
  retiro = saldo - resta
  return retiro

print("Bienvenido al CajeroBancarioTEC, seleccione una opcion:")
print("a. Ingreso")
print("b. Retiro")
print("c. Consulta")
print("d. Salir")

opcion = input()
if opcion == "a":
  suma_input = float(input("Escriba el monto que desea ingresar: "))
  ingreso_total = monto_ingreso(suma_input)
  print(f"Su saldo actual es {ingreso_total}")
if opcion == "b":
  resta_input = float(input("Escriba el monto que desea retirar: "))
  retiro_total = monto_retiro(resta_input)
  print(f"Su saldo actual es {retiro_total}")
if opcion == "c":
  print(f"Su saldo actual es {saldo}")
if opcion == "d":
  print("Que tenga un buen día")
