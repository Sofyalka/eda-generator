#!/usr/bin/env python
# coding: utf-8

# In[6]:

from fastapi import FastAPI, UploadFile, File, HTTPException
from fastapi.responses import FileResponse
import pandas as pd
import os
import tempfile
from eda_generator import generate_eda_report  # импорт из внешнего модуля

app = FastAPI()

@app.post("/upload/")
async def upload_file(file: UploadFile = File(...)):
    filename = file.filename
    extension = filename.split('.')[-1].lower()
    if extension not in ["csv", "xlsx"]:
        raise HTTPException(status_code=400, detail="Формат файла должен быть CSV или Excel")

    with tempfile.NamedTemporaryFile(delete=False, suffix=f".{extension}") as tmp_file:
        tmp_file.write(await file.read())
        temp_file_path = tmp_file.name

    try:
        if extension == "csv":
            df = pd.read_csv(temp_file_path)
        else:
            df = pd.read_excel(temp_file_path)
    except Exception as e:
        os.remove(temp_file_path)
        raise HTTPException(status_code=500, detail=f"Ошибка при чтении файла: {str(e)}")

    os.remove(temp_file_path)

    with tempfile.NamedTemporaryFile(delete=False, suffix=".html") as output_file:
        output_html_path = output_file.name

    try:
        generate_eda_report(df, output_html_path)  # вызываем функцию из отдельного модуля
    except Exception as e:
        os.remove(output_html_path)
        raise HTTPException(status_code=500, detail=f"Ошибка при создании отчета: {str(e)}")

    return FileResponse(path=output_html_path, filename="EDA_Report.html", media_type='text/html')
