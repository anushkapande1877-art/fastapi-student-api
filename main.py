from fastapi import FastAPI

app=FastAPI()

students= {
    1: {"name": "Alice", "branch": "AIML"},
    2: {"name": "Bob", "branch": "CSE"},
    3: {"name": "Charlie","branch": "IT"}
}

@app.get("/students/{student_id}")
def get_student(student_id : int, details : bool=False):

    if student_id not in students:
        return {"error": "Student not found"}

    student = students[student_id]
    if details:
        return {
            "student_id": student_id,
            "name" : student["name"],
            "branch": student["branch"]
        }

    return student
