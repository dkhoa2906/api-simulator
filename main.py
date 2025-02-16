from fastapi import FastAPI, File, UploadFile, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import FileResponse
from pathlib import Path

app = FastAPI()

# Add CORS middleware
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Temporary storage
input_dir = Path("./upload")
input_dir.mkdir(exist_ok=True)

# Pre-saved image for simulation
eg_1 = "eg1.png"
eg_2 = "eg2.png"

@app.post("/swap_hair")
async def swap_hair(
    face_image: UploadFile = File(...),
    hair_shape: UploadFile = File(...),
    hair_color: UploadFile = File(...),
):
    return FileResponse(eg_1, media_type="image/png")

@app.post("/swap_hair_visual")
async def swap_hair_visual(
    face_image: UploadFile = File(...),
    hair_shape: UploadFile = File(...),
    hair_color: UploadFile = File(...),
):
    return FileResponse(eg_2, media_type="image/png")

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)


    # Command to run with Gunicorn:
    # gunicorn -w 4 -k uvicorn.workers.UvicornWorker main:app --bind 0.0.0.0:8000
