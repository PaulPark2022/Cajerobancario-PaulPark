# CajeroBancarioPaulPark

saldo = 5000
suma = 0

#Definicion de la funcion de ingreso
def monto_ingreso(suma):
  ingreso = saldo + suma
  return ingreso

#Definicion de la funcion de retiro
def monto_retiro(resta):
  retiro = saldo - resta
  return retiro

#Cantidad de billetes en el cajero
dict_cajero = {
  "billetes_1000": 1,
  "billetes_500": 2,
  "billetes_200": 5,
  "billetes_100": 10,
  "billetes_50": 20,
  "billetes_20": 50
}

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
        #calculo de cantidad restada al total del cajero
        while resta_input >= 1000 and dict_cajero["billetes_1000"] >= 0:
            resta_input = resta_input - 1000
            dict_cajero["billetes_1000"] -= 1
        dict_cajero["billetes_1000"] *= 1000
        while resta_input >= 500 and dict_cajero["billetes_500"] >= 0:
            resta_input = resta_input - 500
            dict_cajero["billetes_500"] -= 1
        dict_cajero["billetes_500"] *= 500
        while resta_input >= 200 and dict_cajero["billetes_200"] >= 0:
            resta_input = resta_input - 200
            dict_cajero["billetes_200"] -= 1
        dict_cajero["billetes_200"] *= 200
        while resta_input >= 100 and dict_cajero["billetes_100"] >= 0:
            resta_input = resta_input - 100
            dict_cajero["billetes_100"] -= 1
        dict_cajero["billetes_100"] *= 100
        while resta_input >= 50 and dict_cajero["billetes_50"] >= 0:
            resta_input = resta_input - 50
            dict_cajero["billetes_50"] -= 1
        dict_cajero["billetes_50"] *= 50
        while resta_input >= 20 and dict_cajero["billetes_20"] >= 0:
            resta_input = resta_input - 20
            dict_cajero["billetes_20"] -= 1
        dict_cajero["billetes_20"] *= 20
        for billete in dict_cajero:
          suma += dict_cajero[billete]
        print (f"Quedan {suma} pesos en el cajero")
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
