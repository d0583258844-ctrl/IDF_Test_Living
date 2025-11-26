
from fastapi import FastAPI, HTTPException, UploadFile, File
from fastapi.responses import JSONResponse
from soldier_and_base_builders import Soldier
import sqlite3
import io
import csv

app = FastAPI(title = "Soldiers' quarters")

DB_FILE = "info_db.sqlite"


@app.post("/assignWithCsv/")
async def import_csv(file: UploadFile = File(...)):
    tempor_list = []
    if not file.filename.endswith('.csv'):
        raise HTTPException(status_code=400, detail="File must be a CSV file")

    contents = await file.read()
    csv_text = contents.decode('utf-8')
    csv_reader = csv.DictReader(io.StringIO(csv_text))
    for row in csv_reader:
        tempor_list.append(row)
    return tempor_list
        

    
