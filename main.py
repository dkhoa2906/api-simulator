from fastapi import FastAPI, File, UploadFile, HTTPException
from fastapi.responses import Response
import io
import uvicorn

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

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)

    # Command to run with Gunicorn:
    # gunicorn -w 4 -k uvicorn.workers.UvicornWorker fastapi_merge_images:app --bind 0.0.0.0:8000
