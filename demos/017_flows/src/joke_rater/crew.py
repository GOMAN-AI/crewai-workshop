from crewai import Agent, Crew, Task
from crewai.project import CrewBase, agent, crew, task
from .joke_rating import JokeRating

@CrewBase
class JokeRaterCrew():
    @agent
    def comedy_critic_agent(self) -> Agent:
        return Agent(
            config=self.agents_config['comedy_critic'],
        )

    @task
    def rate_joke_task(self) -> Task:
        return Task(
            config=self.tasks_config['rate_joke'],
            agent=self.comedy_critic_agent(),
            output_pydantic=JokeRating,
        )

    @crew
    def crew(self) -> Crew:
        return Crew(
            agents=self.agents,
            tasks=self.tasks,
            verbose=True,
        )
