from typing import Optional
from pydantic import BaseModel
from fastapi import FastAPI

app = FastAPI()
class FirstResponse(BaseModel):
    title: str
    background: str
    option_choices: list[str]
    score: int

@app.get("/")
async def root():
    from openai import OpenAI
    client = OpenAI()
    history = [{ "role": "user", "content": "Please generate a scenario where the UK is under cyber attack. The user will play the role of the UK prime minister having to make choices in response. Initially set the background (~ 250 words) and then at each step give four possible choices (labelled A, B, C, and D) for what choices the user (as PM) can make. Some choices should be good, while others are mistakes. After each step generate what happens next and further choices (both good and bad). The scenario and choices should be understandable by a 14 year old, if there is anything complex, provide an extra explanation. For the first round please generate a scenario title, some background information, and options for what to do, set the player's starting score (that measures how well they are managing the crisis) to 1000. For later rounds (e.g. after the player has responded for the first time) generate a text that gives the players choice, a description of what events happens (~ 150 words) next, and the again options for what to do. Update the player's score based on their choices (a score closer to 1000 indicates perfect handling, a lower score worse handling)."}]
    structure = LaterResponse
    response = client.responses.parse(
        model="gpt-4.1-nano",
        input=history,
        text_format = structure
    )
    return response.output_parsed

@app.get("/items/{item_id}")
def read_item(item_id: int, q: Optional[str] = None):
    return {"item_id": item_id, "q": q}
