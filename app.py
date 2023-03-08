from fastapi import FastAPI
from database import dbConnection
import json

app = FastAPI()

@app.get("/allusers")
def getAllUsers():
    data = dbConnection()
    users = data.connection()
    newUsers = {}
    for user in users:
        newUsers['user'] = user
    return str(users)