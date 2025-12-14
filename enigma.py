import rotors

def menu():
    print("***********************************")
    print("             ENIGMA            ")
    print("***********************************")
    print("       1. Xifrar missatge\n")
    print("     2. Desxifrar missatge\n")
    print("        3. Editar rotors\n")
    print("           4. Sortir")
    print("***********************************\n")

def menu_rotor():
    print()
    print("***********************************")
    print("        MODIFIACIO DE ROTORS")
    print("***********************************")
    print("           1. ROTOR DRET\n")
    print("        2. ROTOR DEL CENTRE\n")
    print("          3. ROTOR ESQUERRA")
    print("***********************************\n")

def resposta_usuari():
    while True:
        try:                                                # Primer que intenti executar aixo, en el cas que sigui un integer seguira.
            usuari = int(input("Escull l'opcio que vols seleccionar: "))
            if 0 < usuari < 5:                              # si l'input de l'usuari es major que 1 o menor que 5, retornara la resposta de l'usuari.
                return usuari
            else:                                           # En el cas contrari, printeara un missatge i tornara a mostrar el menu
                print("Ha de ser un numero mes petit de 5.")
                menu()
        except ValueError:                                  # En el cas que NO sigui un integer, executes el print i la funcio de menu
            print("El valor que s'ha afegit no es el correcta !!!")
            print()
            menu() 
 
def opcio_escollida(usuari):
    if 1 == usuari:                                         # Aquesta funció executa l’opció seleccionada per l’usuari
        xifrar_missatge()
    elif 2 == usuari:
        desxifrar_missatge()
    elif 3 == usuari:
        editar_rotor()
    elif 4 == usuari:
        sortir()
 
def xifrar_missatge():

    simbols = {                                             # * FET AMB AI: per obtenir tots els simbols en un diccionari
    "Á": "A", "À": "A", "Ä": "A", "É": "E", "È": "E", "Ë": "E", "Í": "I", "Ï": "I",
    "Ó": "O", "Ò": "O", "Ö": "O", "Ú": "U", "Ù": "U", "Ü": "U", "Ñ": "N", "Ç": "C", 
    "¡": "", "!": "", "¿": "", "?": "", ",": "", ";": "", ".": "", ":": "", "-": "",
    "_": "", "(": "", ")": "", "[": "", "]": "", "{": "", "}": "", "'": "", "/": "",
    "@": "", "#": "", "$": "", "%": "", "&": "", "*": "", "+": "", "=": "", "<": "",
    ">": "", "·": "", " ": "", "1": "", "2": "", "3": "", "4": "", "5": "", "6": "",
    "7": "", "8": "", "9": "", "0": ""
    }

    while True:
        r = input("Escriu el misatge que vols xifrar: ").upper()
        if r == "":
            print("No has posat res")
            continue
        else:

            frase = ""                                      # String buit per guardar el missatge net

            for lletra in r:                                # Recorre el missatge lletra a lletra
                if lletra in simbols:                       # reempleça simbols i numeros segons el diccionari            
                    frase = frase + simbols[lletra]
                else:
                    frase = frase + lletra

            r1 = rotors.rotor1(frase)                       # Els rotors estan en un altre fitxer anomanat rotors.py
            r2 = rotors.rotor2(r1)
            r3 = rotors.rotor3(r2)

            with open("Xifrat.txt", "w") as xf:             # Escriu el fitxer
                lletras_5 = ""                              # String buit per agrupar lletras de 5 en 5, una vegada xifrat
                for letras in r3:                           # Recorre el missatge xifrat lletra a lletra
                    lletras_5 = lletras_5 + letras          # Copilador de lletras
                    if len(lletras_5) == 5:                 # Quan hi hagi 5 lletres, escriu i afegeix un espai
                        xf.write(lletras_5 + " ")
                        lletras_5 = ""                      # Reiniciem el string a buit
                        
                if len(lletras_5) > 0:                      # Escriu les lletres que hagin sobrat (menor que 5)
                    xf.write(lletras_5)
            break

    with open("Xifrat.txt", "r") as xf:                     # Llegeix el fitxer
        lectura = xf.read()
        lectura = lectura.replace(" ", "").replace("\n", "")# AMB AJUDA DE LA AI: Substitueix una cadena per un altre caracter amb replace
        lletras = len(lectura)                              # Contara les lletras
        lletras_5 = ""
        contador = 0

        for lletra in lectura:                              # Contador de grups de 5
            lletras_5 = lletras_5 + lletra
            if len(lletras_5) == 5:
                contador += 1
                lletras_5 = ""                             

    print("*******************************************************************************")
    print(f"[OK] Missatge xifrat a 'Xifrat.txt' ({lletras} lletres, {contador} grups de 5)")
    print("*******************************************************************************")
                            
def desxifrar_missatge():
    with open("Xifrat.txt", "r") as xf:                 # Llegir el missatge xifrat del fitxer
        missatge_xifrat = xf.read()

                                                            # Eliminar espais i salts de línia per obtenir el text xifrat pur
                                                            # missatge_xifrat_pur és el resultat de rotor3
    missatge_xifrat_pur = missatge_xifrat.replace(" ", "").replace("\n", "")
    
    if not missatge_xifrat_pur:
        print("El fitxer 'Xifrat.txt' està buit.")
        return

    # Aplicar els rotors inversos en ordre invers
    d3_invers = rotors.rotor3_invers(missatge_xifrat_pur)    # Desxifrat R3 invers (Obtenim l'output de R2)
    
    d2_invers = rotors.rotor2_invers(d3_invers)              # Desxifrat R2 invers 

    missatge_desxifrat_net = rotors.rotor1_invers(d2_invers) # Desxifrat R1 invers (Obtenim el missatge original net)
    
    # El missatge desxifrat_net és el missatge sense símbols ni accents.
    
    print("\n*******************************************************************************")
    print(" Missatge Desxifrat (Sense espais, símbols ni accents) ")
    print("*******************************************************************************")
    print(missatge_desxifrat_net)
    print("*******************************************************************************")
    

def editar_rotor():
    
    while True:
        menu_rotor()                                        # Mostra el menu
        resposta = int(input("Quin rotor vols modificar: "))
                                                            # Unicament te tres opcions
        if 0 < resposta == 1 or resposta == 2 or resposta == 3: 
            bucle_rotor(resposta)
            break
        else:
            print("[ERROR] Opció: Aquesta opció no existeix, escull un altre.")
            continue

def bucle_rotor(resposta):

    error = "[ERROR] permutació incorrecta — calen 26 lletres úniques A–Z"

    with open(f"Rotor{resposta}.txt", "w") as rotor:        # Escriu en el fitxer que hi hagi sigut escollit
        while True:
            cablejat = input("Escriu el teu propi cablejat: ").upper()
            if len(cablejat) == 26:
                abcedari = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
                valid = True                                # * FET AMB IA: per detectar errors de validacio

                for lletra in abcedari:                     # Recorre l'abcedari
                    comptador = 0                           # Iniciem comptador
                    for lletra_p in cablejat:               # Recorre el cablejat de l'usuari
                        if lletra_p == lletra:              # Conptara si la lletra es rapateix 
                            comptador += 1  

                    if comptador != 1:                      # * FET AMB IA: per verificar que cada lletra apareix exactament una vegada
                        valid = False                       # *
                        break                               # *


                if valid:                                   # * FET AMB IA per escriure nomes si la permutació és correcta
                    rotor.write(f"{cablejat}\n")
                    while True:
                        notch = input("Escriu la posicio claus (notch) que vols A-Z: ").upper()
                        if notch in abcedari:               # Si la la lletra notch esta en el abcedari 
                            rotor.write(notch)              # Que escrigui la lletra en el fitxer linia 2
                            print("[OK] La teva permutació s'ha guardat correctament")
                            return
                        else:
                            print("[ERROR] Posicio clau incorrecta — úniques A–Z")
                else:
                    print(error)
            else:
                print(error)
           
def sortir():
    exit                                                    # Tancara el programa
