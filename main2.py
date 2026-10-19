
from fastapi import FastAPI
from pydantic import BaseModel, Field

app = FastAPI()


# 1. Define the Pydantic model
class Student(BaseModel):
    name: str = Field(min_length=2, max_length=50)
    age: int = Field(ge=16, le=100)
    branch: str
    github: str | None = None


# 2. Root endpoint
@app.get("/")
def home():
    return {"message": "Student API is running!"}


# 3. GET endpoint
@app.get("/students/example")
def get_example_student():
    return {
        "name": "Tinkle",
        "age": 19,
        "branch": "ECE",
        "github": None
    }


# 4. POST endpoint: receive and validate student data
@app.post("/students")
def create_student(student: Student):
    student_dict = student.model_dump()

    return {
        "message": "Student data received successfully",
        "student": student_dict
    }
