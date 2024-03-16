import grpc
import people_pb2
import people_pb2_grpc

def run():
    channel = grpc.insecure_channel('localhost:8003')
    stub = people_pb2_grpc.PeopleServiceStub(channel)

    # Example: Get all people
    print( "-------------------\n", "Getting all People", "\n-------------------")
    response = stub.GetPeople(people_pb2.GetPeopleRequest())
    print(response, "\n")

    # Example: Get a person by ID
    print("-------------------\n", "Getting Person By Id", "\n-------------------")
    response = stub.GetPerson(people_pb2.GetPersonRequest(id=1))
    print(response)

    # # Example: Add a new person
    # person = people_pb2.Person(id=2, firstName='Jane', lastName='Doe', isAlive=True, age=30)
    # response = stub.AddPerson(people_pb2.AddPersonRequest(person=person))
    # print(response)

    # # Example: Update a person
    # updated_person = people_pb2.Person(id=2, firstName='Jane', lastName='Doe', isAlive=True, age=31)
    # response = stub.UpdatePerson(people_pb2.UpdatePersonRequest(id=2, person=updated_person))
    # print(response)

    # # Example: Delete a person
    # response = stub.DeletePerson(people_pb2.DeletePersonRequest(id=2))
    # print(response)

if __name__ == '__main__':
    run()
