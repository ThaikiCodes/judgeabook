import pandas as pd
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()

# Allowing all middleware is optional, but good practice for dev purposes
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Allows all origins
    allow_credentials=True,
    allow_methods=["*"],  # Allows all methods
    allow_headers=["*"],  # Allows all headers
)

#app.state.model = load_model()

@app.get("/predict")
def predict(image_file
    ):
    #formula
    X_pred_mock = 5
    # model = app.state.model
    # assert model is not None

    # X_processed = preprocess_features(X_pred)
    # y_pred = model.predict(X_processed)
    y_pred_mock = 5 * X_pred_mock

    return y_pred_mock

@app.get("/")
def root():
    # $CHA_BEGIN
    return dict(greeting="Hello, judgeabook")
    # $CHA_END
