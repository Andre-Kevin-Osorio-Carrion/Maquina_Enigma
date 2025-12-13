ALFABET = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"

def rotor1(resposta):
    posicio1 = 0
    lista_rotor1 = ""
 
    with open("Rotor1.txt", "r") as r1:
        alfabet_rotor = r1.readline().strip()  
        p_i = r1.readline().strip()          
 
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
            res = operacio % 26
 
            lista_rotor1 = lista_rotor1 + alfabet_rotor[res]
       
        return lista_rotor1
   
def rotor2(resposta):
    posicio1 = 0
    lista_rotor2 = ""
 
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
            res = operacio % 26
 
            lista_rotor2 = lista_rotor2 + alfabet_rotor[res]
       
        return lista_rotor2
 
def rotor3(resposta):
    posicio1 = 0
    lista_rotor3 = ""
 
    with open("Rotor2.txt", "r") as r3:
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
            res = operacio % 26
 
            lista_rotor3 = lista_rotor3 + alfabet_rotor[res]
       
        return lista_rotor3
 