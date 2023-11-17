def ruota_parola(parola, n):
    global codice
    risultato = ""

    for lettera in parola:
        if lettera.isalpha():
            if lettera.islower():
                codice = ord('a')
            elif lettera.isupper():
                codice = ord('A')

            posizione = ord(lettera) - codice
            nuova_posizione = (posizione + n) % 26
            nuova_lettera = chr(codice + nuova_posizione)
            risultato += nuova_lettera
        else:
            risultato += lettera

    return risultato


def main():
    # Esempio 1
    testo = "Ciao, come stai"
    n = 5
    testo_ruotato = ruota_parola(testo, n)
    print(testo_ruotato)

    # Esempio 2
    testo2 = "Buona giornata"
    n2 = 10
    testo_ruotato2 = ruota_parola(testo2, n2)
    print(testo_ruotato2)

    # Esempio 3
    testo3 = "Il cifrario di Cesare è un metodo di criptazione"
    n3 = -3
    testo_ruotato3 = ruota_parola(testo3, n3)
    print(testo_ruotato3)


if __name__ == '__main__':
    main()