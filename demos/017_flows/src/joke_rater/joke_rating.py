from pydantic import BaseModel, Field

class JokeRating(BaseModel):
    score: int = Field(
        description="A rating of how funny the joke is on a scale from 0 to 100",
        ge=0,  # greater than or equal to 0
        le=100  # less than or equal to 100
    ) 