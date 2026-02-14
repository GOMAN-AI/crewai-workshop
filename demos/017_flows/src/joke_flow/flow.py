from crewai.flow.flow import Flow, listen, start, router, or_
from pydantic import BaseModel
from src.joke_teller.crew import CreateJokeCrew
from src.joke_rater.crew import JokeRaterCrew

class JokeState(BaseModel):
    topic: str = ""
    score: int = 0
    joke: str = ""

class JokeFlow(Flow[JokeState]):
    def __init__(self, topic: str, **kwargs):
        super().__init__(**kwargs)
        self.state.topic = topic

    @start()
    def start(self):
        print("START")

    @listen(or_(start, "new_joke_attempt"))
    def tell_joke(self):
        self.state.score = 0
        result = CreateJokeCrew().crew().kickoff(inputs={"topic": self.state.topic})
        self.state.joke = result.pydantic.joke

    @listen(tell_joke)
    def evaluate_joke(self):
        result = JokeRaterCrew().crew().kickoff(inputs={"joke": self.state.joke})
        self.state.score = result.pydantic.score

    @router(evaluate_joke)
    def decide_if_joke_good(self):
        if self.state.score >= 75:
            return self.state.joke
        else:
            return "new_joke_attempt"
