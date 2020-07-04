"""
Main server file for the API.
For request/response format specification, see api_spec.py.
See README for running instructions.
"""
import importlib

from fastapi import FastAPI, HTTPException

import api_spec
#from storage import database

app = FastAPI()

# @app.post("/board", response_model=??, response_model_exclude_unset=True)
# async def generate(request: ??):