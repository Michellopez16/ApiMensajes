from fastapi import FastAPI
import numpy as np

app = FastAPI()


@app.get("/")
async def root():
    return {"message": np.random.randint(0, 100000)}

@app.get("/users/{user_id}")
async def read_user(user_id: str):
    num = np.random.randint(0, 100000)
    print("user_id: {}".format(user_id))
    return {"message": num}