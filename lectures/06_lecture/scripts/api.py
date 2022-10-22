#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
API service for STRV DS Academy purpose; written in FastAPI.

To run the API locally, follow these steps:

1. Start API by the following command: uvicorn api:app --reload
2. Check the Titanic survival model endpoint here: http://127.0.0.1:8000/survival_proba
3. Check documentation here: http://127.0.0.1:8000/docs
"""

import os
import pickle
import time

from enum import Enum
import pandas as pd
from fastapi import FastAPI, Query

MODEL_PATH = os.path.join(
    os.path.dirname(__file__),
    "../titanic/model.pickle"
)

# load model
with open(MODEL_PATH, "rb") as input_file:
    model = pickle.load(input_file)

# app description
description = """
Titanic survival model predicts what is the passanger probability to survive
the biggest marine catastrophe in mankind history.

### Model

- RandomForest binary classifier.
- Built with one and only scikit-learn library.
- Accuracy on test dataset equals to 75 %.
"""

# define FastAPI app
app = FastAPI(
    title="🛳️ Titanic survival model API",
    description=description,
    version="0.0.1",
    contact={
        "name": "STRV DS Department",
        "url": "http://www.strv.com",
        "email": "datascience.dept@strv.com",
    },
    license_info={
        "name": "Apache 2.0",
        "url": "https://www.apache.org/licenses/LICENSE-2.0.html",
    },
)

# define gender data type
class GenderDataType(str, Enum):
    MALE = "Male"
    FEMALE = "Female"
    NON_BINARY = "Non-binary"
    TRANSGENDER = "Transgender"
    INTERSEX = "Intersex"
    NOT_SAY = "Preferred not to say"

# define API endpoint /proba
@app.get("/survival_proba")
async def get_survival_proba(
    pass_class: int = Query(
        default=1,
        ge=1,
        le=3,
        description="Passenger's class",
    ),
    pass_gender: GenderDataType = "Male",
    pass_age: int = Query(
        default=0,
        ge=0,
        le=100,
        description="Passenger's age",
    ),
    pass_sib_sp_cnt: int = Query(
        default=0,
        ge=0,
        le=10,
        description="Passenger's number of siblings/spouse",
    ),
    pass_par_child_cnt: int = Query(
        default=0,
        ge=0,
        le=10,
        description="Passenger's number of parents/children",
    ),
    pass_fare: int = Query(
        default=0,
        ge=0,
        le=750,
        description="Passenger's fare",
    ),
):
    start_time = time.time()

    # get input data frame
    passenger_to_predict = pd.DataFrame([
        {
            "class": pass_class,
            "age": pass_age,
            "sib_sp_cnt": pass_sib_sp_cnt,
            "par_child_cnt": pass_par_child_cnt,
            "fare": pass_fare,
            "is_male": int(pass_gender == "Male"),
        },
    ])

    # return survival probability
    survival_proba = model.predict_proba(passenger_to_predict)[0][0] * 100

    return {
        "processing_time": round(time.time() - start_time, 4),
        "timestamp": int(time.time()),
        "survival_proba": round(survival_proba, 2),
        "model_input_data": passenger_to_predict.to_dict(orient="records")
    }
