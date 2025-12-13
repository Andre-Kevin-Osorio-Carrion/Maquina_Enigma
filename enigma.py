import rotors

def menu():
    print("             ENIGMA            ")
    print("-------------------------------")
    print("       1. Xifrar missatge      ")
    print()
    print("     2. Desxifrar missatge     ")
    print()
    print("        3. Editar rotors       ")
    print()
    print("           4. Sortir           ")
    print()
 
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
        ...
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
                            
def desxifrar_missatge():
    ...

def editar_rotor():
    ...

def sortir():
    exit #Tancara el programa





