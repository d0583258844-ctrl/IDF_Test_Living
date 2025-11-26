
from fastapi import FastAPI, UploadFile, File
from fastapi.responses import JSONResponse
import os

app = FastAPI(title = "Soldiers'_quarters")
UPLOAD_DIR = "uploads"
os.makedirs(UPLOAD_DIR, exist_ok=True)

@app.post("/assignWithCsv/")
async def import_csv(file: UploadFile = File(...)):
    if not file.filename.endswith('.csv'):
        return JSONResponse(
            status_code=400,
            content={"error": "רק קבצי CSV מותרים"}
        )    
    file_path = os.path.join(UPLOAD_DIR, file.filename)

    with open(file_path, "wb") as f:
        content = await file.read()
        f.write(content)
    
    return {
        "message": "הקובץ הועלה בהצלחה!",
        "filename": file.filename,
        "size": len(content),
        "path": file_path
    }
