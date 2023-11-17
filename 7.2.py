def evalCiclo(continua):
    mem = ''
    while continua != 'fatto':
        mem = continua
        print(eval(continua))
        continua = input('espressione:')

    print(eval(mem))

def main():
    continua = input('espressione:')
    evalCiclo(continua)




if __name__ == '__main__':
    main()