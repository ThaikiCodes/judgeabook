from fastapi import FastAPI, Request, HTTPException, status
from fastapi.responses import HTMLResponse
from judgeabook.ml_logic.data import Data
from deepface import DeepFace
import base64
import json
import cv2

import numpy as np

data = Data()
data.load_data()

app = FastAPI()
app.data = data


@app.post("/files/")
async def create_files(
    request: Request,                                       # https://github.com/tiangolo/fastapi/issues/3327 (read image from request)
):
    image = await request.body()

    nparr = np.asarray(bytearray(image), dtype="uint8")     # https://www.geeksforgeeks.org/python-opencv-imdecode-function/ (convert bytes to image)
    image = cv2.imdecode(nparr, cv2.IMREAD_COLOR)

    obj = DeepFace.analyze(img_path=image, actions=('age','emotion'))

    # obj = [{'age': 41, 'region': {'x': 260, 'y': 470, 'w': 959, 'h': 959}, 'emotion': {'angry': 9.047427695918486e-07, 'disgust': 1.8703599206118223e-15, 'fear': 5.437250584668096e-11, 'happy': 99.982351064682, 'sad': 1.7980640976134055e-06, 'surprise': 1.4686735028135445e-05, 'neutral': 0.0176409404957667}, 'dominant_emotion': 'happy'}]

    if len(obj) == 0:
        raise HTTPException(                                # https://stackoverflow.com/questions/68270330/how-to-return-status-code-in-response-correctly
            status_code=status.HTTP_404_NOT_FOUND,
            detail="failed to analyze image",
        )

    age = obj[0].get("age")
    emotion = obj[0].get("dominant_emotion")
    zodiac = app.data.get_attributes(age, emotion)
    response = json.dumps(zodiac.__dict__)

    return response


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
