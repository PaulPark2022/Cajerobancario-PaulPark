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

#Pantalla de inicio
print("Bienvenido al CajeroBancarioTEC, seleccione una opcion:")
print("a. Ingreso")
print("b. Retiro")
print("c. Consulta")
print("d. Salir")

#Ejecucion de todas las opciones
acum = 0
while acum < 10:
  opcion = input()
  if opcion != "a" and opcion != "b" and opcion != "c" and opcion != "d":
    print("Esta seleccion no es valida")
    print("Bienvenido al CajeroBancarioTEC, seleccione una opcion:")
    print("a. Ingreso")
    print("b. Retiro")
    print("c. Consulta")
    print("d. Salir")
  else:
    if opcion == "a":
      suma_input = float(input("Escriba el monto que desea ingresar: "))
      ingreso_total = monto_ingreso(suma_input)
      print(f"Su saldo actual es {ingreso_total}")
      acum += 1
      saldo = ingreso_total
      print("Bienvenido al CajeroBancarioTEC, seleccione una opcion:")
      print("a. Ingreso")
      print("b. Retiro")
      print("c. Consulta")
      print("d. Salir")
    if opcion == "b":
      resta_input = float(input("Escriba el monto que desea retirar: "))
      if resta_input > 5000:
        print("No puede retirar una cantidad mayor a su saldo")
        print("Bienvenido al CajeroBancarioTEC, seleccione una opcion:")
        print("a. Ingreso")
        print("b. Retiro")
        print("c. Consulta")
        print("d. Salir")
      else:
        retiro_total = monto_retiro(resta_input)
        print(f"Su saldo actual es {retiro_total}")
        acum += 1
        saldo = retiro_total
        print("Bienvenido al CajeroBancarioTEC, seleccione una opcion:")
        print("a. Ingreso")
        print("b. Retiro")
        print("c. Consulta")
        print("d. Salir")
    if opcion == "c":
      print(f"Su saldo actual es {saldo}")
      acum += 1
      print("Bienvenido al CajeroBancarioTEC, seleccione una opcion:")
      print("a. Ingreso")
      print("b. Retiro")
      print("c. Consulta")
      print("d. Salir")
    if opcion == "d":
      acum += 10
else:
  print("Que tenga un buen día")
