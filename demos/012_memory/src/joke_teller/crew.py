import os
from crewai import Agent, Crew, Task
from crewai.project import CrewBase, agent, crew, task

@CrewBase
class CreateJokeCrew():
    def __init__(self, user: str):
        self.user = user

    @agent
    def comedian_agent(self) -> Agent:
        return Agent(
            config=self.agents_config['comedian'],
        )

    @task
    def create_joke_task(self) -> Task:
        return Task(
            config=self.tasks_config['create_joke'],
            agent=self.comedian_agent(),
        )

    @crew
    def crew(self) -> Crew:
        return Crew(
            agents=self.agents,
            tasks=self.tasks,
            verbose=True,
            memory=True,
            embedder={
                "provider": "openai",
                "config": {
                    "api_key": os.getenv("OPENAI_API_KEY"),
                    "model": "text-embedding-3-large",
                    "dimensions": 1536,
                }
            }

        )
