import random
from time import sleep

nome = input(' Digite seu nome :').upper()
b = random.randint(0, 100)

print(' Bom dia {}'.format(nome))
jogar = str(input('Gostaria de jogar ?  \n \33[32m[1] SIM \33[36m[2] NAO \n'))

while jogar == '1' or jogar == 'sim':
    print('\33[33m+++++++++++++++++++++')
    print('JOGO DE ADIVINHAÇÃO')
    print('+++++++++++++++++++++')
    print('\33[mIniciando em 3')
    sleep(1)
    print('              __2')
    sleep(1)
    print('                  _1')
    sleep(1)
    numero = int(input('Primeiramente pense e digite um numero :'))
    sleep(2)
    print('depois o multiplique por 2')
    multiplique = numero * 2
    sleep(2)
    adicao1 = input('E adicione +{}_'.format(b))
    adicao = multiplique + b
    sleep(2)
    print('Depois divida o resultado por 2')
    dividir = adicao / 2
    sleep(2)
    print('Diminua o resultado menos o numero que voce pensou')
    subtrair = dividir - numero
    print(print('{} * 2 + {} /2 - {} igual a'.format(numero,b,numero)))
    sleep(3)

    print('\33[34m++++++++++=====================++++++++++++++')
    print('O resultado sera {:.1f}'.format(b/2))
    resultado = b/2
    print('++++++++++=====================++++++++++++++')
    acertei = resultado
    acertei = input('\33[m acertei?   \33[32m[1] SIM \33[36m[2] NAO \33[m\n')
    if acertei == '1' or acertei == 'sim':
        print('\33[31mPode dizer eu sou demais')
        break
    elif acertei == '2' or acertei == 'nao':
        print('tenha paciencia e tente novamente')
        break
    else:
        print('parece que voce nao aprendeu a ler...Pois so havia duas opções.')
        break
while jogar == '2' or jogar == 'nao':
    certeza = input('\33[m Certeza que vc não quer jogar??? \n \33[32m[1] SIM \33[36m[2] NAO  \n')
    if certeza == '1' or certeza == 'sim':
        print('\33[35mVoce é chato heim!!!')
        sleep(1)
        print('Voce é chato heim!!!')
        sleep(2)
        print('{}, Voce é muito chato!!!'.format(nome))
        break
    else:
        print('\33[31mVá para o inicio e tente novamente.')
        break
