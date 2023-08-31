from fastapi import FastAPI, Request
from fastapi.responses import HTMLResponse
from deepface import DeepFace
import base64
import json
import cv2

import numpy as np

app = FastAPI()


@app.post("/files/")
async def create_files(
    request: Request,                                       # https://github.com/tiangolo/fastapi/issues/3327 (read image from request)
):
    image = await request.body()

    nparr = np.asarray(bytearray(image), dtype="uint8")     # https://www.geeksforgeeks.org/python-opencv-imdecode-function/ (convert bytes to image)
    image = cv2.imdecode(nparr, cv2.IMREAD_COLOR)

    obj = DeepFace.analyze(img_path=image, actions=('age',))
    response = json.dumps(obj)

    return {"response": response}


@app.get("/")
async def main():
    content = """
<body>
<form action="/files/" enctype="multipart/form-data" method="post">
<input name="files" type="file" multiple>
<input type="submit">
</form>
</body>
    """
    return HTMLResponse(content=content)

if __name__ == "__main__":
    import uvicorn

    uvicorn.run(app, host="0.0.0.0", port=8000)
