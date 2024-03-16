from flask import Flask
from graphene import ObjectType, String, Int, List, Schema, Field, Mutation, Boolean
from flask_graphql import GraphQLView

app = Flask(__name__)


people_data = [
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


# Define your GraphQL schema
class Person(ObjectType):
    _id = Int()
    firstName = String()
    lastName = String()
    isAlive = Boolean()
    age = Int()
    address = String()
    phoneNumbers = List(String)
    children = List(String)
    spouse = String()

class Query(ObjectType):
    people = List(Person, _id=Int())
    person_by_id = Field(Person, _id=Int(required=True))


    def resolve_people(self, info, _id=None):
        if _id is not None:
            # If _id is provided, return the person with that _id
            for person in people_data:
                if person['_id'] == _id:
                    return [person]
            return None
        else:
            # If _id is not provided, return all people
            return people_data

# class PersonInput(InputObjectType):
#     _id = Int()
#     firstName = String()
#     lastName = String()
#     isAlive = String()
#     age = Int()
#     address = String()
#     phoneNumbers = List(String)
#     children = List(String)
#     spouse = String()
    
class CreatePerson(Mutation):
    firstName = String()
    lastName = String()
    isAlive = Boolean()
    age = Int()
    address = String()
    phoneNumbers = List(String)
    children = List(String)
    spouse = String()

    class Arguments:
        firstName = String()
        lastName = String()
        isAlive = Boolean()
        age = Int()
        address = String()
        phoneNumbers = List(String)
        children = List(String)
        spouse = String()

    def mutate(self, info, firstName, lastName, isAlive, age, address, phoneNumbers, children, spouse):
        new_person = Person(firstName=firstName, lastName=lastName, isAlive=isAlive, age=age, address=address, phoneNumbers=phoneNumbers, children=children, spouse=spouse)
        new_person["_id"] = len(people_data)  # Generate a new ID for the person
        people_data.append(new_person)
        return CreatePerson(person=new_person)

class Mutation(ObjectType):
    create_person = CreatePerson().Field()
    
    
schema = Schema(query=Query,  mutation=Mutation)

# Create a view for the GraphQL API
app.add_url_rule('/graphql', view_func=GraphQLView.as_view('graphql', schema=schema, graphiql=True))

if __name__ == '__main__':
    app.run(debug=True, port=8002)
