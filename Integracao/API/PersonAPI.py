from flask import Flask, jsonify, request

app = Flask(__name__)

people = [
    {'nome': 'João', 'idade': 30, 'cpf': '10245798741'},
    {'nome': 'Rodrigo', 'idade': 20, 'cpf': '10668794941'},
    {'nome': 'Maria', 'idade': 24, 'cpf': '11444566987'}
]


@app.route('/people', methods=['POST'])
def create_person():
    new_person = request.json
    people.append(new_person)

    return jsonify({'mensagem': 'Pessoa criada com sucesso!'})


@app.route('/people', methods=['GET'])
def read_people():
    return jsonify(people)


@app.route('/people/<int:person_id>', methods=['PUT'])
def update_person(person_id):
    person = people[person_id]
    if person:
        person.update(request.json)
        return jsonify({'mensagem': 'Pessoa atualizada com sucesso!'})
    else:
        return jsonify({'mensagem': 'Pessoa não encontrada!'}), 404


@app.route('/people/<int:person_id>', methods=['DELETE'])
def delete_person(person_id):
    person = person = people[person_id]
    if person:
        people.remove(person)
        return jsonify({'mensagem': 'Pessoa excluída com sucesso!'})
    else:
        return jsonify({'mensagem': 'Pessoa não encontrada!'}), 404


app.run(debug=True)
