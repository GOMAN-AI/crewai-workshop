from crewai import Agent, Crew, Task
from crewai.project import CrewBase, agent, crew, task
from joke_with_explanation import JokeWithExplanation
from crewai_tools import ScrapeWebsiteTool

@CrewBase
class CreateJokeCrew():
    @agent
    def comedian_agent(self) -> Agent:
        return Agent(
            config=self.agents_config['comedian'],
            tools=[ScrapeWebsiteTool()],
        )

    @task
    def create_joke_task(self) -> Task:
        return Task(
            config=self.tasks_config['create_joke'],
            agent=self.comedian_agent(),
            output_pydantic=JokeWithExplanation,
        )

    @crew
    def crew(self) -> Crew:
        return Crew(
            agents=self.agents,
            tasks=self.tasks,
            verbose=True,
        )
