from pydantic import BaseModel

class JokeWithExplanation(BaseModel):
    joke: str
    explanation: str
    youtube_video_url: str
