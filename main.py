from fastapi import FastAPI

app = FastAPI()

@app.get("/")
async def read_root():
    return {"message": "Hello, world!"}

@app.get("/students")
async def get_students():
    # Example static data; replace with DB or other source as needed
    return [
        {"id": 1, "name": "Alice", "major": "Computer Science"},
        {"id": 2, "name": "Bob", "major": "Mathematics"},
        {"id": 3, "name": "Charlie", "major": "Physics"},
    ]
