from crewai import Agent, Crew, Task
from crewai.project import CrewBase, agent, crew, task
from joke_with_explanation import JokeWithExplanation
from .tools import YouTubeSearchToolWrapper
from crewai_tools import ScrapeWebsiteTool

@CrewBase
class CreateJokeCrew():
    @agent
    def channel_researcher(self) -> Agent:
        return Agent(
            config=self.agents_config['channel_researcher'],
            tools=[YouTubeSearchToolWrapper()],
        )

    @agent
    def videos_researcher(self) -> Agent:
        return Agent(
            config=self.agents_config['videos_researcher'],
            tools=[ScrapeWebsiteTool()],
        )

    @agent
    def comedian_agent(self) -> Agent:
        return Agent(
            config=self.agents_config['comedian'],
        )

    @task
    def find_latest_videos(self) -> Task:
        return Task(
            config=self.tasks_config['find_latest_videos'],
            agent=self.channel_researcher(),
        )

    @task
    def fetch_videos_information(self) -> Task:
        return Task(
            config=self.tasks_config['fetch_videos_information'],
            agent=self.videos_researcher(),
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
