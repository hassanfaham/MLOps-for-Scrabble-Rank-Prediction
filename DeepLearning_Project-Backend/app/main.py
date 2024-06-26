from fastapi import FastAPI
import tensorflow as tf
from uvicorn import run
import os
from pathlib import Path
import numpy as np
import h5py
from pydantic import BaseModel
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()

origins = [
    "http://localhost:80",
    "http://localhost:4200"
]
app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


BASE_DIR = Path(__file__).resolve(strict=True).parent

model = tf.keras.models.load_model(str(BASE_DIR)+"/scrabble_model.h5",compile=False)
model.compile()
#model = h5py.File(str(BASE_DIR)+"/scrabble_model.h5", mode='r')

class Features(BaseModel):
    N_games_played : int
    mean_points_per_round : float
    mean_move_length : float
    first_to_play : bool
    winner : bool


@app.get("/ping")
async def pong():
    return {"ping": "pong!"}


@app.post("/predict")
def ranking_prediction(player: Features):

    prediction = model.predict([[374, 
                        player.N_games_played, 
                        player.mean_points_per_round, 
                        28.034, 
                        7.0, 
                        player.mean_move_length, 
                        8.0, 
                        0.136, 
                        0.075, 
                        -0.605, 
                        -0.457, 
                        0.059, 
                        0.501, 
                        6.564, 
                        0.49, 
                        0.57, 
                        0.925, 
                        0.026, 
                        0.035, 
                        0.006, 
                        0.007, 
                        0.0, 
                        0.0, 
                        0.0, 
                        13, 
                        player.first_to_play, 
                        player.winner, 
                        1155.645, 
                        0, 
                        1, 
                        465.165, 
                        0, 
                        0, 
                        1, 
                        0, 
                        0, 
                        0, 
                        1, 
                        0, 
                        1, 
                        0, 
                        0, 
                        0, 
                        0, 
                        1]])
    print(player)
    return {"prediction": int(prediction)}

if __name__ == "__main__":
	port = int(os.environ.get('PORT', 8008))
	run(app, host="0.0.0.0", port=port)


#uvicorn main:app --reload --workers 1 --host 0.0.0.0 --port 8008