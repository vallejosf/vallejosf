import os 
os.system("cls")

print("")
print("┌──────────────────────────────────────────────────────────────┐")
print("|🏥Buenvenidxs al sistema de historias Clinicas del Hospital🏥 |")
print("└──────────────────────────────────────────────────────────────┘")
print("")

# ********************
# *global variables*
# ********************

running = True 
# database = list()
database = [{'nombre': 'Fernando', 'historia': 'Dolor de espalda'}, {'nombre': 'Pedro', 'historia': 'Dolor de cabeza'}]



# ********************
# *    FUNCTIONS     *
# ********************

def show_menu():
    print("")
    print("")
    print("\t\t🔴  1 - Cargar paciente")
    print("\t\t🔴  2 - Buscar paciente")
    print("\t\t🔴  3 - Listar pacientes")
    print("\t\t🔴  4 - Salir")
    print("")
    res = input("INGRESE UNA OPCION ► ")
    return res

def response_validated(r):
    validated = False
    num_res = 0

    if response.isdigit():
        num_res = int(response)
        if num_res >= 1 and num_res <= 4:
            msg = "Esta en rango"
            validated = True
        else:
            msg = "Fuera de rango"
    else: 
        msg ="Entrada incorrecta"
    
    return validated,num_res,msg

# ********************
# *  MAIN LOOP  *
# ********************

while running:
    response = show_menu()
    validated,num_res,msg=response_validated(response)
    if validated:
        if num_res == 1:
            name = input("Ingrese el nombre del paciente ► ")
            history = input("Ingrese la historia clinica del paciente ► ")
            paciente = {"nombre":name, "historia":history}
            database.append(paciente)
            print(database)
        
        elif num_res == 2:
            name = input("Ingrese el nombre del paciente ► ")

            finded = True
            for x in range(len(database)):
                if  database[x]["nombre"].lower() == name.lower():
                    print("")
                    print("Paciente encontrado!")
                    print("PACIENTE ENCONTRADO | H. CLINICA ► ",database[x]["historia"])
                    print("")
                else:
                    finded = False
                    if not finded:
                        print ("Paciente no encontrado, por favor verifique su busqueda")      
            

        elif num_res == 3:
            print("")
            print("┌───────────────────────┐")
            print("|  LISTADO DE PACIENTES |")
            print("└───────────────────────┘")
            print("")
            for x in range(len(database)):
                print("Nombre ► ".ljust(10),database[x]["nombre"],"\tHistoria C. ► ".ljust(10),database[x]["historia"])

            print("FIN DE LISTA")

        else:
            running = False
    else:
        print(msg)
        
print("")
print("Aplicacion Finalizada")
print("")
