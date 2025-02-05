from fastapi import FastAPI, File, UploadFile, HTTPException
from fastapi.responses import Response
import io

app = FastAPI()

@app.post("/process/")
async def upload_images(
        face: UploadFile = File(...),
        shape: UploadFile = File(...),
        color: UploadFile = File(...),
):
    try:
        img_bytes = await color.read()

        return Response(content=img_bytes, media_type=color.content_type)

    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))