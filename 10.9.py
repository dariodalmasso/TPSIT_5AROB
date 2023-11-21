import time

def leggi_file_append(file_name):
    parole = []
    with open(file_name, 'r') as file:
        for linea in file:
            parole.extend(linea.strip().split())
    return parole

def leggi_file_concatenazione(file_name):
    parole = []
    with open(file_name, 'r') as file:
        for linea in file:
            parole = parole + linea.strip().split()
    return parole

def main():
    file_name = 'words.txt'

    start_time = time.time()
    parole_append = leggi_file_append(file_name)
    end_time = time.time()

    tempo_append = end_time - start_time

    start_time = time.time()
    parole_concatenazione = leggi_file_concatenazione(file_name)
    end_time = time.time()

    tempo_concatenazione = end_time - start_time

    print(f"Tempo impiegato con append(): {tempo_append} secondi")
    print(f"Tempo impiegato con concatenazione: {tempo_concatenazione} secondi")

    if tempo_append > tempo_concatenazione:
        print('funzione APPEND più veloce')
    else:
        print('funzione CONCATENAZIONE più veloce')


if __name__ == '__main__':
    main()

"""
Per quanto riguarda la domanda sulla quale versione richiede più tempo di esecuzione, 
generalmente la versione con il metodo append è più efficiente rispetto alla concatenazione 
con il costrutto t = t + [x]. Questo perché il metodo append aggiunge un elemento alla fine 
della lista in modo più ottimizzato rispetto alla concatenazione, che richiede la creazione 
di una nuova lista a ogni iterazione.
"""