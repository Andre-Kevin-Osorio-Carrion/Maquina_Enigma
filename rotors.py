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