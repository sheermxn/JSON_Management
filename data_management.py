import json
from os.path import dirname, realpath, isfile
from os import system
from time import sleep

dir = dirname(realpath(__file__)) + '/'
user_os = str(input('Informe seu OS:\n(w) - Windows | (l) - Linux e derivados\n--> '))

def Limpar_Console():
    if user_os == 'w':
        try:
            system("cls")
        except:
            print('Erro ao limpar console.')
            choose = str(input('Deseja retornar a escolha de OS? y/n: '))
            if str.lower(choose) == 'y':
                return user_os
            elif str.lower(choose) == 'n':
                Limpar_Console()
            else:
                print('Erro.')
                Limpar_Console()
    elif user_os == 'l':
        try:
            system("clear")
        except:
            print('Erro ao limpar console.')
            choose = str(input('Deseja retornar a escolha de OS? y/n: '))
            if str.lower(choose) == 'y':
                return user_os
            elif str.lower(choose) == 'n':
                Limpar_Console()
            else:
                print('Erro.')
                Limpar_Console()
    else:
        print('Erro ao limpar console.')

def Main_Menu():
    print("Sistema de Gerenciamento JSON\n(1) - Listar arquivo JSON\n(2) - Adicionar dado JSON\n(3) - Deletar dado JSON\n(4) - Abortar")
    while True:
        sleep(.1)
        select = int(input('\n--> '))
        if select == 1:
            print('=' * 18)
            sleep(1)
            Limpar_Console()
            List_Data('data/data.json', 'nil')
            break
        elif select == 2:
            print('=' * 18)
            sleep(1)
            Limpar_Console()
            Add_Data('data/data.json')
            break
        elif select == 3:
            print('=' * 18)
            sleep(1)
            Limpar_Console()
            Rm_Data('data/data.json')
            break
        elif select == 4:
            break
        else:
            print('Opção inválida, por favor leia com calma.')

def List_Data(file, returning):
    path = dir + file
    with open (path, "r") as f:
        temp = json.load(f)
        index = 0
        for info in temp:
            print(f'Index: {str(index)}')
            print(f'Username: {info["username"]}\nPassword: {info["password"]}\n\n')
            print('=' * 18)
            index = index + 1
    if returning == 'rm':
        pass
    else:
        Change_Menu()
    
def Add_Data(file):
    path = dir + file
    user_data = {}
    with open (path, "r") as f:
        temp = json.load(f)
    user_data["username"] = input('Usuário: ')
    user_data["password"] = input('Senha: ')
    temp.append(user_data)
    with open (path, "w") as f:
        json.dump(temp, f, indent=2)
    print('=' * 18)
    Change_Menu()

def Rm_Data(file):
    path = dir + file
    List_Data('data/data.json', 'rm')
    newdata = []
    with open (path, "r") as f:
        temp = json.load(f)
        length = len(temp)-1
    index_choose = int(input(f'Qual index gostaria de remover 0-{length}?\n--> '))
    i = 0
    for entry in temp:
        if i == index_choose:
            pass
            i = i + 1
        else:
            newdata.append(entry)
            i = i + 1
    with open (path, "w") as f:
        json.dump(newdata, f, indent=2)
    Change_Menu()
    
def Change_Menu():
    print("(1) - Listar arquivo JSON\n(2) - Adicionar dado JSON\n(3) - Deletar dado JSON\n(4) - Abortar")
    select = int(input('\n--> '))
    if select == 1:
        print('=' * 18)
        sleep(1)
        Limpar_Console()
        List_Data('data/data.json', 'nil')
    elif select == 2:
        print('=' * 18)
        sleep(1)
        Limpar_Console()
        Add_Data('data/data.json')
    elif select == 3:
        print('=' * 18)
        sleep(1)
        Limpar_Console()
        Rm_Data('data/data.json')
    elif select == 4:
        exit()
    else:
        print('Opção inválida, por favor leia com calma.')
        print('=' * 18)
        sleep(1)
        Limpar_Console()
        Change_Menu()

if __name__ == "__main__":
    Main_Menu()