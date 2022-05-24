from fastapi import FastAPI


app = FastAPI()


@app.get("/")
def greets_a_person():
    return {"greetings": "hey!"}
