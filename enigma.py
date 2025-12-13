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

def resposta_usauri():
    while True:
        try: #Primero que intente ejecutar esto en el caso que sea un int seguira.
            usuari = int(input("Escull l'opcio que vols seleccionar: "))
            if 0 < usuari < 5: # si el input del usuari es mayor que 1 o menor que 5, devolvera la respuesta del usuario.
                return usuari
            else: # En el caso contrario, printeara un mensaje y volvera a mostrar el menu
                print("Ha de ser un numero mes petit de 5.")
                menu()
        except ValueError: # En el caso que NO sea un int, ejecutara el print y la funcion de menu
            print("El valor que s'ha afegit no es el correcta !!!")
            print()
            menu() 
 
def opcio_escollida(usuari):
    if 1 == usuari:
        xifrar_missatge()
    elif 2 == usuari:
        desxifrar_missatge()
    elif 3 == usuari:
        editar_rotor()
    elif 4 == usuari:
        sortir()
 
def xifrar_missatge():

    simbols = { #FET AMB AI per obtenir tots els simbols en un diccionari
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
            frase = ""

            for lletra in r:
                if lletra in simbols:
                    frase = frase + simbols[lletra]
                else:
                    frase = frase + lletra

            r1 = rotors.rotor1(frase)
            r2 = rotors.rotor2(r1)
            r3 = rotors.rotor3(r2)

            with open("Xifrat.txt", "w") as xf:
                letras_5 = ""
                for letras in r3:
                    letras_5 = letras_5 + letras
                    if len(letras_5) == 5:
                        xf.write(letras_5 + " ")
                        letras_5 = ""
                        
                if len(letras_5) > 0:
                    xf.write(letras_5)
            break

    with open("Xifrat.txt", "r") as xf:
        lectura = xf.read()
        lectura = lectura.replace(" ", "").replace("\n", "")
        lletras = len(lectura)
        lletras_5 = ""
        contador = 0

        for lletra in lectura:
            lletras_5 = lletras_5 + lletra
            if len(lletras_5) == 5:
                contador += 1
                lletras_5 = ""

    print("*******************************************************************************")
    print(f"[OK] Missatge xifrat a 'Xifrat.txt' ({lletras} lletres, {contador} grups de 5)")
    print("*******************************************************************************")
                            
def desxifrar_missatge():
    ...

def editar_rotor():
    
    while True:
        menu_rotor()
        resposta = int(input("Quin rotor vols modificar: "))

        if 0 < resposta == 1 or resposta == 2 or resposta == 3:
            bucle_rotor(resposta)
            break
        else:
            print("[ERROR] Opció: Aquesta opció no existeix, escull un altre.")
            continue

def bucle_rotor(resposta):

    error = "[ERROR] permutació incorrecta — calen 26 lletres úniques A–Z"

    with open(f"Rotor{resposta}.txt", "w") as rotor:
        while True:
            cablejat = input("Escriu el teu propi cablejat: ").upper()
            if len(cablejat) == 26:
                abcedari = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
                valid = True  # FET AMB IA per detectar errors de validacio

                for lletra in abcedari:
                    comptador = 0  
                    for lletra_p in cablejat:
                        if lletra_p == lletra:
                            comptador += 1  

                    if comptador != 1:  # FET AMB IA per verificar que cada lletra apareix exactament una vegada
                        valid = False
                        break


                if valid:  # FET AMB IA per escriure nomes si la permutació és correcta
                    rotor.write(f"{cablejat}\n")
                    while True:
                        notch = input("Escriu la posicio claus (notch) que vols A-Z: ").upper()
                        if notch in abcedari:
                            rotor.write(notch)
                            print("[OK] La teva permutació s'ha guardat correctament")
                            return
                        else:
                            print("[ERROR] Posicio clau incorrecta — úniques A–Z")
                else:
                    print(error)
            else:
                print(error)
           
def sortir():
    exit #Tancara el programa
