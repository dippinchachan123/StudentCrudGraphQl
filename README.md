# Django GraphQL Student CRUD Operations

This project provides a simple CRUD (Create, Read, Update, Delete) operations for managing student records using Django and GraphQL. It allows you to perform basic operations such as adding, viewing, updating, and deleting student information.

## Getting Started

Follow these instructions to get a copy of the project up and running on your local machine for development and testing purposes.

### Prerequisites

Ensure you have the following software installed on your machine:
- Python (version 3.x)
- Django
- Graphene-Django

### Installation


1. Create a virtual environment (optional but recommended):
   python -m venv venv

2. Activate the virtual environment:
   - On Windows:
     venv\Scripts\activate
   - On macOS and Linux:
     source venv/bin/activate


### Database Setup

1. Apply database migrations:
   python manage.py migrate

### Running the Development Server

Start the Django development server:
   python manage.py runserver

The server should now be running at `http://127.0.0.1:8000/`.

### Accessing GraphQL Interface

You can access the GraphQL interface at `http://127.0.0.1:8000/graphql/`. This interface allows you to interact with the GraphQL API for performing CRUD operations on student records.

## GraphQL Schema

The GraphQL schema defines the available queries and mutations for interacting with student data. You can explore the schema and execute queries/mutations using the GraphQL interface provided by Django.

### Example Query

query {
  students {
    id
    name
    age
    rollno
    student_class
    gender
  }
}

### Example Mutation

mutation {
  createStudent(
    name: "John Doe",
    age: 20,
    rollno: "12345",
    studentClass: "10",
    gender: "M"
  ) {
    student {
      id
      name
      age
      rollno
      student_class
      gender
    }
  }
}

## Contributing

Contributions are welcome! If you find any issues or have suggestions for improvements, feel free to open an issue or submit a pull request.

## License

This project is licensed under the MIT License.
