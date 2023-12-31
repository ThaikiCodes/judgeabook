from fastapi import FastAPI, Request, HTTPException, status
from fastapi.responses import HTMLResponse
from judgeabook.ml_logic.data import Data
from deepface import DeepFace
import base64
import json
import cv2

import numpy as np

data = Data()
data.load_data()  # carrega o dataframe vindo do GCS

app = FastAPI()
app.data = data


@app.post("/files/")
async def create_files(
    request: Request,                                       # https://github.com/tiangolo/fastapi/issues/3327 (read image from request)
):
    image = await request.body()     #ler a requisiçao,

    nparr = np.asarray(bytearray(image), dtype="uint8")     # https://www.geeksforgeeks.org/python-opencv-imdecode-function/ (convert bytes to numpy array)
    image = cv2.imdecode(nparr, cv2.IMREAD_COLOR)     # converteu o numpy array para imagem

    obj = DeepFace.analyze(img_path=image, actions=('age','emotion')) # Analise da imagem considerando emocoes e idade

    # obj = [{'age': 41, 'region': {'x': 260, 'y': 470, 'w': 959, 'h': 959}, 'emotion': {'angry': 9.047427695918486e-07, 'disgust': 1.8703599206118223e-15, 'fear': 5.437250584668096e-11, 'happy': 99.982351064682, 'sad': 1.7980640976134055e-06, 'surprise': 1.4686735028135445e-05, 'neutral': 0.0176409404957667}, 'dominant_emotion': 'happy'}]

    if len(obj) == 0:  # Se o retorno da analise for vazio, retorna para o frontend um erro 404
        raise HTTPException(                                # https://stackoverflow.com/questions/68270330/how-to-return-status-code-in-response-correctly
            status_code=status.HTTP_404_NOT_FOUND,
            detail="failed to analyze image",
        )

    age = obj[0].get("age")                      # le a idade retornada pela analise do deepface
    emotion = obj[0].get("dominant_emotion")     # le a emocao retornada pela analise do deepface
    zodiac = app.data.get_attributes(age, emotion) # Utiliza o dataframe baixado do GCS para verificar qual é o signo a partir da idade
    response = json.dumps(zodiac.__dict__)        # converte o zodiac para um json que vamos retornar para o frontend

    return response     # retorna o json para o frontend


# @app.get("/")      # Pagina de teste, nao precisamos
# async def main():
#     content = """
# <body>
# <form action="/files/" enctype="multipart/form-data" method="post">
# <input name="files" type="file" multiple>
# <input type="submit">
# </form>
# </body>
#     """
#     return HTMLResponse(content=content)

if __name__ == "__main__":
    import uvicorn

    uvicorn.run(app, host="0.0.0.0", port=8000)
