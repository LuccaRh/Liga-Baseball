from fastapi import FastAPI
from pydantic import BaseModel
import psycopg2
import os
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)
class League(BaseModel):
    name: str

@app.post("/leagues")
def create_league(league: League):

    conn = psycopg2.connect(
        database=os.getenv("POSTGRES_DB"),
        user=os.getenv("POSTGRES_USER"),
        password=os.getenv("POSTGRES_PASSWORD"),
        host=os.getenv("POSTGRES_HOST"),
        port=os.getenv("POSTGRES_PORT")
    )

    cur = conn.cursor()

    cur.execute(
        "INSERT INTO ligas (name) VALUES (%s)",
        (league.name,)
    )

    conn.commit()
    cur.close()
    conn.close()

    return {"message": "League created"}
