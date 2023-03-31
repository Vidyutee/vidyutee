from fastapi import FastAPI
from backend import setup
from pydantic import BaseModel
import pandas as pd
from typing import Optional
import backend.scheduler as scheduler
from datetime import date


# app initialize
app = FastAPI()


class UserID(BaseModel):
    uid: str
    appliance_data: str

# class Test(BaseModel):
#     name: str

# @app.post("/")
# def func(test: Test):
#     return {"name": test.name}

@app.post("/")
def func(user: UserID):
    data = setup.db.collection('users').document(user.uid).get().to_dict()
    appliance_set = user.appliance_data
    dt = str(date.today())
    try:
        test = data[f"{'_'.join(appliance_set.split())}_schedule"][dt]
        return test
    except:
        schedule = scheduler.schedule(data[appliance_set])
        setup.db.collection('users').document(user.uid).update(
            {f"{'_'.join(appliance_set.split())}_schedule": {dt: schedule}})
        return setup.db.collection('users').document(user.uid).get().to_dict()[f"{'_'.join(appliance_set.split())}_schedule"][dt]

