import math

def stima_pi():
    approx_pi = 0
    k = 0
    while True:
        numerator = math.factorial(4*k) * (1103 + 26390*k)
        denominator = math.factorial(k)**4 * 396**(4*k)
        term = numerator / denominator
        approx_pi += term

        if abs(term) < 1e-15:
            break

        k += 1

    approx_pi = 1 / ((2 * math.sqrt(2) / 9801) * approx_pi)
    return approx_pi

def main():
    # Calcola l'approssimazione di π
    pi_approximation = stima_pi()

    # Confronta con il valore di math.pi
    print("Approssimazione di π:", pi_approximation)
    print("math.pi:", math.pi)

if __name__ == "__main__":
    main()

