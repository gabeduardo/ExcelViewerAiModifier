from fastapi import FastAPI, UploadFile, File, Form
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import StreamingResponse
from fastapi.responses import JSONResponse
from app.excel_utils import get_sheet_names, extract_sheet_data, write_excel
from app.modifier import apply_rules_with_llm
import io
import json

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.post("/upload")
async def upload_excel(file: UploadFile = File(...)):
    contents = await file.read()
    sheet_names = get_sheet_names(contents)
    return {"sheets": sheet_names}

@app.post("/export")
async def modify_excel(file: UploadFile = File(...), sheet: str = Form(...)):
    contents = await file.read()
    data = extract_sheet_data(contents, sheet)
    modified_data = apply_rules_with_llm(data)
    output = write_excel({sheet: modified_data})

    return StreamingResponse(
        io.BytesIO(output),
        media_type="application/vnd.openxmlformats-officedocument.spreadsheetml.sheet",
        headers={"Content-Disposition": "attachment; filename=modified.xlsx"}
    )


@app.get("/sample-data")
async def get_sample_data():
    try:
        with open("app/rules.json", "r", encoding="utf-8") as f:
            rules = json.load(f)
        return JSONResponse(content=rules)
    except Exception as e:
        return JSONResponse(content={"error": str(e)}, status_code=500)