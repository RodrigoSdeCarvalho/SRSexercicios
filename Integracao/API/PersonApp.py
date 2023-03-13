import requests
import json

def create_person():
    name = input('Digite o nome da pessoa: ')
    age = int(input('Digite a idade da pessoa: '))
    cpf = input('Digite o cpf da pessoa: ')
    new_person = {'nome': name, 'idade': age, 'cpf': cpf}
    response = requests.post('http://localhost:5000/pessoas', json=new_person)
    if response.status_code == 200:
        print('Pessoa criada com sucesso!')
    else:
        print('Erro ao criar pessoa')


def search_person():
    person_id = int(input('Digite o ID da pessoa que deseja pesquisar: '))
    response = requests.get('http://localhost:5000/pessoas')
    people = json.loads(response.content)
    try:
        person = people[person_id]
        print(f'ID: {person_id}, Nome: {person["nome"]}, Idade: {person["idade"]}, cpf: {person["cpf"]}')
    except:
        print('Pessoa não encontrada')


def read_people():
    response = requests.get('http://localhost:5000/pessoas')
    poeple = json.loads(response.content)
    for id, person in enumerate(poeple):
        print(f'ID: {id}, Nome: {person["nome"]}, Idade: {person["idade"]}, cpf: {person["cpf"]}')


def update_person():
    person_id = int(input('Digite o ID da pessoa que deseja atualizar: '))
    person = {'nome': input('Digite o nome da pessoa: '), 'idade': int(input('Digite a idade da pessoa: ')), 'cpf': input('Digite o cpf da pessoa: ')}
    response = requests.put(f'http://localhost:5000/pessoas/{person_id}', json=person)
    if response.status_code == 200:
        print('Pessoa atualizada com sucesso!')
    else:
        print('Erro ao atualizar pessoa')


def delete_person():
    person_id = int(input('Digite o ID da pessoa que deseja excluir: '))
    response = requests.delete(f'http://localhost:5000/pessoas/{person_id}')
    if response.status_code == 200:
        print('Pessoa excluída com sucesso!')
    else:
        print('Erro ao excluir pessoa')


while True:
    print('\nEscolha uma opção:')
    print('1 - Cadastrar Pessoa')
    print('2 - Atualizar Pessoa')
    print('3 - Pesquisar Pessoa')
    print('4 - Excluir Pessoa')
    print('5 - Listar Pessoas')
    print('0 - Sair')
    opcao = input('Opção: ')
    if opcao == '1':
        create_person()
    elif opcao == '2':
        update_person()
    elif opcao == '3':
        search_person()
    elif opcao == '4':
        delete_person()
    elif opcao == '5':
        read_people()
    elif opcao == '0':
        break
    else:
        print('Opção inválida')
