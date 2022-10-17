# CajeroBancarioPaulPark

#Funcion de pantalla de inicio
def menu_cajero():
  print("Bienvenido al CajeroBancarioTEC, seleccione una opción: ")
  print("a. Ingreso")
  print("b. Retiro")
  print("c. Consulta")
  print("d. Salir")
  opcion = (input("Opción --> "))
  return opcion

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

#Historial de movimientos
historial_ingresos = ["Sus ingresos anteriores fueron: "]
historial_retiros = ["Sus retiros anteriores fueron: "]
historial_movimientos = [historial_ingresos,historial_retiros]

#Ejecucion de todas las opciones
opcion = menu_cajero()
while opcion != "d":
    if opcion == "a":
      suma_input = float(input("Escriba el monto que desea ingresar: "))
      ingreso_total = monto_ingreso(suma_input)
      print(f"Su saldo actual es {ingreso_total}")
      saldo = ingreso_total
      historial_ingresos.append(ingreso_total)
    elif opcion == "b":
      resta_input = float(input("Escriba el monto que desea retirar: "))
      if resta_input > 5000:
        print("No puede retirar una cantidad mayor a su saldo")
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
        saldo = retiro_total
        historial_retiros.append(retiro_total)
    elif opcion == "c":
      print(f"Su saldo actual es {saldo}")
    else:
      print("Opción no válida")

    opcion = menu_cajero()

    print(historial_movimientos)
