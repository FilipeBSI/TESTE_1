from time import sleep


def mensagem():
    print('=' * 20)
    print('--BOM DIA-- ')
    print('=' * 20)

def pergunta_empresa():
    empresa = str(input('Digite o nome da sua empresa : ')).upper().split()
    return empresa
def pergunta_nome():
    nome = str(input('Digite seu nome: '))
    return nome
def wait(nome,empresa):
    sleep(2)



mensagem()
pergunta_nome()
pergunta_empresa()




    