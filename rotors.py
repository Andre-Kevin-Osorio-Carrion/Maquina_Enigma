ALFABET = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"

def rotor1(resposta):
    posicio1 = 0
    lista_rotor1 = ""                                           # String buit per guardar el resultat del rotor
    rang_abcedari = 26

    with open("Rotor1.txt", "r") as r1:
        alfabet_rotor = r1.readline().strip()                   # Llegeix el cablejat del rotor (Linia 1)
        p_i = r1.readline().strip()                             # Llegeix la posició inicial (Linia 2)
 
        for x in ALFABET:                                       # Troba la posició inicial dins l'alfabet
            if p_i == x:
                break
            posicio1 += 1
 
        for lletras in resposta:                                # Recorre cada lletra del missatge
            posicio2 = 0
 
            for x in ALFABET:                                   # Troba la posició de la lletra dins l'alfabet
                if lletras == x:
                    break
                posicio2 += 1
 
            operacio = posicio1 + posicio2                      # Sumem les posicions 
            res = operacio % rang_abcedari                      # I calculem el residu per mantenir-ho dins l'alfabet
 
            lista_rotor1 = lista_rotor1 + alfabet_rotor[res]    # Afagirem al string buit que vam crear al principi
            posicio1 = (posicio1 + 1) % rang_abcedari           # Movem una posicion del rotor i verfiquem que estigui dins del rang del abcedari
       
        return lista_rotor1
   
def rotor2(resposta):
    posicio1 = 0
    lista_rotor2 = ""
    rang_abcedari = 26
 
    with open("Rotor2.txt", "r") as r2:
        alfabet_rotor = r2.readline().strip()
        p_i = r2.readline().strip()            
 
        for x in ALFABET:  
            if p_i == x:
                break
            posicio1 += 1
 
        for lletras in resposta:
            posicio2 = 0
 
            for x in ALFABET:
                if lletras == x:
                    break
                posicio2 += 1
 
            operacio = posicio1 + posicio2
            res = operacio % rang_abcedari
 
            lista_rotor2 = lista_rotor2 + alfabet_rotor[res]
            posicio1 = (posicio1 + 1) % rang_abcedari
       
        return lista_rotor2
 
def rotor3(resposta):
    posicio1 = 0
    lista_rotor3 = ""
    rang_abcedari = 26
 
    with open("Rotor3.txt", "r") as r3:
        alfabet_rotor = r3.readline().strip()
        p_i = r3.readline().strip()            
 
        for x in ALFABET:  
            if p_i == x:
                break
            posicio1 += 1
 
        for lletras in resposta:
            posicio2 = 0
 
            for x in ALFABET:
                if lletras == x:
                    break
                posicio2 += 1
 
            operacio = posicio1 + posicio2
            res = operacio % rang_abcedari
 
            lista_rotor3 = lista_rotor3 + alfabet_rotor[res]
            posicio1 = (posicio1 + 1) % rang_abcedari
       
        return lista_rotor3

def rotor_invers(missatge_xifrat, nom_fitxer_rotor):            #Lògica inversa genèrica per a un sol rotor.
    
    posicio1 = 0
    missatge_desxifrat = ""
    rang_abcedari = 26

    with open(nom_fitxer_rotor, "r") as r:                      # Llegeix el cablejat i la posició inicial del fitxer
            alfabet_rotor = r.readline().strip()                # Cablejat del rotor (Línia 1)
            p_i = r.readline().strip()                          # Posició inicial (Línia 2)

    posicio1 = ALFABET.find(p_i)                                # Troba la posició inicial (offset) dins l'alfabet

    for lletras_xifrada in missatge_xifrat:                     # Desxifra cada lletra
        
        idx_in_rotor = alfabet_rotor.find(lletras_xifrada)      # Trobem l'índex de la lletra xifrada dins del cablejat del rotor
        
        if idx_in_rotor == -1:                                  # Si no és una lletra, l'afegim 
            missatge_desxifrat += lletras_xifrada
            
        else:                                                   # Calculem l'índex de la lletra original (posicio2) amb la fórmula inversa
            posicio2 = (idx_in_rotor - posicio1 + rang_abcedari) % rang_abcedari
            
            missatge_desxifrat += ALFABET[posicio2]             # La lletra desxifrada és la que es troba en posicio2 de l'ALFABET

        posicio1 = (posicio1 + 1) % rang_abcedari               # Movem el rotor (ROTACIÓ)

    return missatge_desxifrat


# Funcion inversa per a cada rotor
def rotor1_invers(missatge_xifrat):
    return rotor_invers(missatge_xifrat, "Rotor1.txt")

def rotor2_invers(missatge_xifrat):
    return rotor_invers(missatge_xifrat, "Rotor2.txt")

def rotor3_invers(missatge_xifrat):
    return rotor_invers(missatge_xifrat, "Rotor3.txt")
