print('*************************************************************')
print('%%%%%%%%%%%%%%%%---BEM VINDO AO JOGO---%%%%%%%%%%%%%%%%%%%%%%')
print('*************************************************************')

print('Olá sou ALEXIA... Seu assistente.')
nome = str(input('Digite seu nome:')).strip().upper()
sexo = input('Sexo ? [M/F]')
idade = int(input('Qual sua idade?'))

familia = str('SANTOS')
familia = str(input('Por favor digite seu sobrenome :')).strip().upper()

if familia == 'SANTOS':
    if nome == 'AMANDA':
        print('\33[31m {}, ja tinha visto nomes bonitos mas esse foi demais '.format(nome))
    elif nome == 'RAQUEL':
        print('\33[31m {}, Ja tinha visto coisas feias...Mas tu supera qualquer uma delas!!!'.format(nome))
    elif nome == 'ISABEL':
        print('\33[31m {}, fecha a boca cobra venenosa.Ta escorrendo o veneno !!!'.format(nome))
    elif nome == 'MARIA':
        print('\33[31m{}, Se voce veio ate aki é muito provável que me deve um pix de R$100'.format(nome))
    elif nome == 'MANOEL':
        print('\33[31m {}, Cachorros nao latem mas magoam'.format(nome))
    elif nome == 'FILIPE':
        print('\33[31m {}, Perdão alteza.Mas voce é demais'.format(nome))
    else:
        print('\33[m {} Perdão mas voce não faz parte dessa familia.'.format(nome))
        print('Desculpe mas nao posso lhe ajudar')

# idades
    if idade <= 12:
        print('\33[mParabens {} voce tem {} anos e ainda é um criança!!!'.format(nome, idade))
    elif 13 <= idade <= 30:
        print('Parabens {} voce tem {} anos e ainda é jovem'.format(nome, idade))
    elif 32 <= idade < 50:
        print('Parabens {} voce tem {} anos e já é um adulto'.format(nome, idade))
    elif idade >= 52:
        print('Parabens {} voce tem {} anos e já esta ficando velho(a) demais'.format(nome, idade))
    else:
        print('desculpe nao consegui intender '
              'tente novamente')
# Piadas
    p = input('Tenho piadas prontas, gostaria de ouvi-las?').upper().strip()[0]
    if p == 'SIM':
        if nome == 'AMANDA':
            print('Sabe o que o rato diz quando se queima ?')
            print('Nossa MICKEY MEI !')
        if nome == 'RAQUEL':
            print('Qual o cereal favorito do vampiro?')
            print('Aveia')
        if nome == 'ISABEL':
            print('O que a xuxa foi fazer no bar??')
            print('foi beber ca sasha')
        if nome == 'MARIA':
            print('Se a vida estiver muito amarga, da uma rebolada. As vezes o açúcar esta no fundo!!! ')
        if nome == 'MANOEL':
            print('Qual a diferença entre uma bicicleta e uma privada?')
            print('A bicicleta voce senta pra correr e a privada voce corre pra sentar. !')
        if nome == 'FILIPE':
            print('voce fez aquilo que gostaria.')
        else:
            print('Infelizmente nao tenho piadas pra voce.')
    else:
        print('Que falta de senso de humor heim!!')
        print('desculpe nao consegui intender '
              'tente novamente')

else:
    print('Desculpe mas seu nome e sobrenome nao estão cadastrado')

