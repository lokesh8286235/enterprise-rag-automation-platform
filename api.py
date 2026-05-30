from fastapi import FastAPI
from src.agent import Agent

app = FastAPI()

agent = Agent()

@app.get("/ask")
def ask(query: str):

    return agent.answer(query)
