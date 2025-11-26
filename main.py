
from fastapi import FastAPI, HTTPException, UploadFile, File
from fastapi.responses import JSONResponse
from soldier_and_base_builders import Soldier, Room
from operator import itemgetter
import sqlite3
import io
import csv

app = FastAPI(title = "Soldiers' quarters")

DB_FILE = "info_db.sqlite"

tempor_list = []

@app.post("/assignWithCsv")
async def my_import_csv(file: UploadFile = File(...)):
    
    if not file.filename.endswith('.csv'):
        raise HTTPException(status_code=400, detail="File must be a CSV file")

    contents = await file.read()
    csv_text = contents.decode('utf-8')
    csv_reader = csv.DictReader(io.StringIO(csv_text))
    for row in csv_reader:
        tempor_list.append(row)
        row["distance"]=int(row["distance"])
    return (sort_solder_by_KM(tempor_list))

    
def sort_solder_by_KM(list_soldiers: list[dict]) -> list[dict]:
    return sorted(list_soldiers, key=itemgetter('distance'),reverse=True)


a = Room()
a.add_soldier(tempor_list)
print(a)