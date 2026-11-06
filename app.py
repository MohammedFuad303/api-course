from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

#first test with creating an API
@app.get("/")
def home():
    return {"message" : "Hello, I am your first API."}



#input the name and delivers it
@app.get("/hello/{name}")
def say_hello(name: str):
    return {"message" : f"Hello, {name}!"}


#same input but with numbers
@app.get("/double/{number}")
def double(number: int):
    return {"result" : number * 2}

tasks = []

class Task(BaseModel):
    title: str
    done : bool = False


@app.post("/tasks")
def check_task(task: Task):
    tasks.append(task)
    return {"message" : "Task saved", "total_tasks" : len(tasks)}


@app.get("/tasks")
def get_tasks():
    return tasks


if __name__ == "__main__":
    home()