import grpc
from concurrent import futures
import people_pb2
import people_pb2_grpc

# Define your data here
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

class PeopleServicer(people_pb2_grpc.PeopleServiceServicer):
    def GetPeople(self, request, context):
        # Implement logic to fetch all people
        response = people_pb2.GetPeopleResponse()
        for person_data in people_data:
            person = response.people.add()
            person.id = person_data["_id"]
            person.firstName = person_data["firstName"]
            person.lastName = person_data["lastName"]
            person.isAlive = person_data["isAlive"]
            person.age = person_data["age"]
            # Add other fields as needed
        return response

    def GetPerson(self, request, context):
        # Implement logic to fetch a single person by ID
        response = people_pb2.Person()
        for person_data in people_data:
            if person_data["_id"] == request.id:
                response.id = person_data["_id"]
                response.firstName = person_data["firstName"]
                response.lastName = person_data["lastName"]
                response.isAlive = person_data["isAlive"]
                response.age = person_data["age"]
                # Add other fields as needed
                break
        return response

    # Implement other CRUD operations similarly

def serve():
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
    people_pb2_grpc.add_PeopleServiceServicer_to_server(PeopleServicer(), server)
    server.add_insecure_port('[::]:8003')
    print("Server running on port - 8003")
    server.start()
    server.wait_for_termination()

if __name__ == '__main__':
    serve()
