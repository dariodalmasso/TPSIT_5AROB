import random

def genera_compleanni(n):
    return [random.randint(1, 365) for _ in range(n)]  # 365 giorni in un anno, ignorando gli anni bisestili

def ha_duplicati(compleanni):
    return len(compleanni) != len(set(compleanni))

def main():
    numero_simulazioni = 10000
    contatore_duplicati = 0

    for _ in range(numero_simulazioni):
        compleanni = genera_compleanni(23)
        if ha_duplicati(compleanni):
            contatore_duplicati += 1

    probabilita = contatore_duplicati / numero_simulazioni
    print(f"La probabilità stimata di avere almeno due studenti con la stessa data di compleanno è {probabilita:.2%}")

if __name__ == "__main__":
    main()
