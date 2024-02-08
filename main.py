from fastapi import FastAPI, HTTPException, status
from enum import Enum

app = FastAPI()


class GenreURLChoices(Enum):
    ROCK = 'rock'
    ELECTRONIC = 'electronic'
    METAL = 'metal'
    HIP_HOP = 'hip-hop'


BANDS = [
    {'id': '1', 'name': 'John', 'genre': 'Rock'},
    {'id': '2', 'name': 'Anna', 'genre': 'Electronic'},
    {'id': '3', 'name': 'Ali', 'genre': 'Metal'},
    {'id': '4', 'name': 'Jack', 'genre': 'Hip-Hop'}
]


@app.get("/bands")
async def bands() -> list[dict]:
    return BANDS


@app.get("/bands/{band_id}")
async def band_(band_id: int) -> dict:
    band = next((b for b in BANDS if b['id'] == str(band_id)), None)
    if band is None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail='Band not found')
    return band


@app.get('bands/genre/{genre}')
async def bands_for_genre(genre: GenreURLChoices) -> list[dict]:
    return [b for b in BANDS if b['genre'].lower() == genre.value]
