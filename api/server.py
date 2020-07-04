"""
Main server file for the API.
For request/response format specification, see api_spec.py.
See README for running instructions.
"""
import importlib

from fastapi import FastAPI, HTTPException, Path, Query

import api_spec
#from storage import database

app = FastAPI()

@app.get("/all_tasks")
async def get_all_tasks():
    results = {1,2,3}
        #get tasks from db, filler data rn

    return results


@app.get("/")
async def root():
    """
    Root route. Currently just responds to a GET request with a message.
    Useful for testing that your server is working; will require a
    different response before deployment.
    """
    return {"message": "yes this is dog"}