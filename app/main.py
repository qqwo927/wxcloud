from fastapi import FastAPI, File, UploadFile
import os
app = FastAPI()
UPLOAD_FOLDER = 'uploads'
# 确保上传文件夹存在
if not os.path.exists(UPLOAD_FOLDER):
    os.makedirs(UPLOAD_FOLDER)
@app.post("/upload/")
async def upload_file(file: UploadFile = File(...)):
    filepath = os.path.join(UPLOAD_FOLDER, file.filename)
    with open(filepath, "wb") as buffer:
        buffer.write(await file.read())
    return {"filename": file.filename}
if __name__ == '__main__':
    import uvicorn
    uvicorn.run(app, host="127.0.0.1", port=80)

