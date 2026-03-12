from fastapi import FastAPI
from pydantic import BaseModel
import psycopg2

app = FastAPI()

class League(BaseModel):
    name: str

@app.post("/leagues")
def create_league(league: League):

    conn = psycopg2.connect(
        database="liga",
        user="postgres",
        password="123",
        host="localhost"
    )

    cur = conn.cursor()

    cur.execute(
        "INSERT INTO leagues (name) VALUES (%s)",
        (league.name,)
    )

    conn.commit()
    cur.close()
    conn.close()

    return {"message": "League created"}