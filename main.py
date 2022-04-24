from typing import Optional
from pydantic import BaseModel

from fastapi import FastAPI
from proximity_analysis import proximity_analysis

app = FastAPI()


@app.get("/prox/{a}")
async def create_process(a:int):
    # Logic to save the response in csv
    #process_list = [process.csv_name,process.number]
    result = proximity_analysis.prox(a)
    return result
