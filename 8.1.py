def main():
    text = "   ciao, mondo!   "
    stripped_text = text.strip()
    print(stripped_text)

    text = "ciao, mondo!"
    new_text = text.replace("ciao", "salve")
    print(new_text)

if __name__ == '__main__':
    main()