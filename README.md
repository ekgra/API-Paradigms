A comparison of various API Paradigms using a simple CRUD example

- REST

- GraphQL
  
  Env 

    ```
    python=3.9`
    pip install Flask-GraphQL
    pip install graphene=2.1.9
    ```
 
 GraphiQL Interface

    http://localhost:8002/graphql

  Query

    {"query": "{ people { Id firstName lastName } }"}

  Mutation

    mutation {
    createPerson( firstName: "Jane", lastName: "Doe", isAlive: false, age: 30, address: "unknown", phoneNumbers: ["unknown"], children: ["none"], spouse: "none" ) {
        firstName
        lastName
        isAlive
        age
        address
        phoneNumbers
        children
        spouse
    }
    }

- grpc

    ```
    pip install grpcio-tools
    python -m grpc_tools.protoc -I . --python_out=. --grpc_python_out=. ./people.proto
    ```

    ```
    python grpcServer.py
    python grpcClient.py
    ```
