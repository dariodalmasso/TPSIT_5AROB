def is_bifronte(parola):
    return parola == parola[::-1]

def trova_parole_bifronti(lista_parole):
    parole_bifronti = []
    for parola in lista_parole:
        if is_bifronte(parola):
            parole_bifronti.append(parola)
    return parole_bifronti

lista_parole_italiane = ["radar", "livello", "anna", "otto", "pera"]
#lista_parole_italiane = ["livello", "pera"]

parole_bifronti = trova_parole_bifronti(lista_parole_italiane)

if len(parole_bifronti) > 0:
    print("Parole bifronti trovate:")
    for parola in parole_bifronti:
        print(parola)
else:
    print("Nessuna parola bifronte trovata nella lista.")
