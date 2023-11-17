import re

# Funzione per cercare parole con tre coppie di lettere uguali consecutive
def cerca_parole_con_coppie_consecutive(lista):
    risultato = []
    for parola in lista:
        if re.search(r'(.)\1(.)\2(.)\3', parola):
            risultato.append(parola)
    return risultato

def main():
    # Lista di parole inglesi
    lista_parole = ["bookkeeping", "programming", "success", "committee", "bookkeeper"]

    # Trova le parole con tre coppie di lettere uguali consecutive
    parole_con_coppie = cerca_parole_con_coppie_consecutive(lista_parole)

    # Stampare le parole trovate
    if parole_con_coppie:
        print("Parole con tre coppie di lettere uguali consecutive:")
        for parola in parole_con_coppie:
            print(parola)
    else:
        print("Nessuna parola con tre coppie di lettere uguali consecutive trovata.")

if __name__ == "__main__":
    main()
