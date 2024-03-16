from flask import Flask, jsonify, request

app = Flask(__name__)

# Sample data
people = [
    {
        "_id": 0,
        "firstName": "John",
        "lastName": "Smith",
        "isAlive": True,
        "age": 27,
        "address": {
            "streetAddress": "21 2nd Street",
            "city": "New York",
            "state": "NY",
            "postalCode": "10021-3100"
        },
        "phoneNumbers": [
            {
                "type": "home",
                "number": "212 555-1234"
            },
            {
                "type": "office",
                "number": "646 555-4567"
            }
        ],
        "children": ["Catherine", "Thomas", "Trevor"],
        "spouse": None
    },
    {
        "_id": 1,
        "firstName": "Albert",
        "lastName": "Einstein",
        "isAlive": False,
        "age": 100,
        "address": {
            "streetAddress": "some street",
            "city": "Berlin",
            "state": "Germany",
            "postalCode": "10021-3100"
        },
        "phoneNumbers": [
            {
                "type": "home",
                "number": "999 999-999"
            },
            {
                "type": "office",
                "number": "646 555-4567"
            }
        ],
        "children": None,
        "spouse": "cousin"
    }
]


# CRUD operations
@app.route('/people', methods=['GET'])
def get_people():
    return jsonify(people)


@app.route('/people/<int:person_id>', methods=['GET'])
def get_person(person_id):
    person = next((p for p in people if p['_id'] == person_id), None)
    if person:
        return jsonify(person)
    else:
        return jsonify({"error": "Person not found"}), 404


@app.route('/people', methods=['POST'])
def add_person():
    person_data = request.get_json()
    people.append(person_data)
    return jsonify({"message": "Person added successfully"}), 201


@app.route('/people/<int:person_id>', methods=['PUT'])
def update_person(person_id):
    person_data = request.get_json()
    for index, person in enumerate(people):
        if person['_id'] == person_id:
            people[index] = person_data
            return jsonify({"message": "Person updated successfully"})
    return jsonify({"error": "Person not found"}), 404


@app.route('/people/<int:person_id>', methods=['DELETE'])
def delete_person(person_id):
    global people
    people = [p for p in people if p['_id'] != person_id]
    return jsonify({"message": "Person deleted successfully"})


if __name__ == '__main__':
    app.run(debug=True, port=8001)
