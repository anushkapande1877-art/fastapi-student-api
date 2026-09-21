# FastAPI Student API

A simple FastAPI project to learn path parameters and query parameters.

## Features

* Get student information using a student ID
* Demonstrates path parameters
* Demonstrates query parameters
* Basic error handling

## Run the Project

```bash
pip install fastapi uvicorn
uvicorn main:app --reload
```

## API Endpoints

### Get Student

```http
GET /students/{student_id}
```

Example:

```http
/students/1
```

Response:

```json
{
  "name": "Alice",
  "branch": "AIML"
}
```

### Get Student Details

```http
/students/1?details=true
```

Response:

```json
{
  "student_id": 1,
  "name": "Alice",
  "branch": "AIML"
}
```

## What I Learned

* Creating APIs with FastAPI
* Path Parameters
* Query Parameters
* Returning JSON responses
* Basic API testing
