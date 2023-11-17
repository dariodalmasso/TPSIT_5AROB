def main():
    def ePalindrom0(word):
        return word == word[::-1]

    parola = "cuneo"
    if ePalindrom0(parola):
        print(f"{parola} è un palindromo.")
    else:
        print(f"{parola} non è un palindromo.")

if __name__ == '__main__':
    main()