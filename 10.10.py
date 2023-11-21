def bisezione(lista_ordinata, valore_da_cercare):
    primo = 0
    ultimo = len(lista_ordinata) - 1

    while primo <= ultimo:
        medio = (primo + ultimo) // 2
        parola_media = lista_ordinata[medio]

        if parola_media == valore_da_cercare:
            return True
        elif parola_media < valore_da_cercare:
            primo = medio + 1
        else:
            ultimo = medio - 1

    return False

def main():
    elenco_parole = [
        "abbandonare", "abbigliamento", "abbondante", "accendere", "acqua", "affettuoso",
        "agricoltura", "aiutare", "albero", "amico", "andare", "animale", "anniversario",
        "appartamento", "arrivare", "arte", "attimo", "aumentare", "auto", "autunno", "azienda",
        "bagno", "barca", "bello", "bene", "bicicletta", "cane", "casa", "cibo", "città", "colore",
        "comprare", "condominio", "corpo", "cucina", "cultura", "danza", "dentista", "desiderio",
        "difficile", "dire", "dolce", "domani", "eccellente", "economia", "educazione", "esame",
        "famiglia", "felice", "fiore", "fotografia", "fratello", "fresco", "gioia", "giorno", "governo",
        "grande", "hobby", "hotel", "importante", "informazione", "insegnante", "italiano", "lavoro",
        "libro", "macchina", "mare", "matematica", "medicina", "miele", "montagna", "musica", "natura",
        "navigare", "notte", "occasione", "occhio", "palestra", "passeggiata", "paziente", "perdere",
        "pesce", "pianoforte", "pioggia", "polizia", "preoccupazione", "ragazza", "regalo", "relazione",
        "riposo", "salute", "scienza", "sera", "sorriso", "spiaggia", "stazione", "studiare", "teatro",
        "telefono", "tempo", "tennis", "triste", "università", "vacanza", "vino", "vita", "volare", "zaino"
    ]

    parola_da_cercare = 'fiore'

    if bisezione(elenco_parole, parola_da_cercare):
        print(f"{parola_da_cercare} è presente nell'elenco.")
    else:
        print(f"{parola_da_cercare} non è presente nell'elenco.")


if __name__ == '__main__':
    main()
