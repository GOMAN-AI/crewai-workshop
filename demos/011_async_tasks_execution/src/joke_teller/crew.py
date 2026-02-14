from crewai import Agent, Crew, Task
from crewai.project import CrewBase, agent, crew, task
from joke_with_explanation import JokeWithExplanation
from videos_information import VideosInformation
from .tools import YouTubeSearchToolWrapper, WikipediaSearchToolWrapper
from crewai.tasks.task_output import TaskOutput
from crewai.tasks.conditional_task import ConditionalTask
from crewai_tools import SerperDevTool, ScrapeWebsiteTool
from typing import Any, Dict, List, Tuple, Union


@CrewBase
class CreateJokeCrew():
    @agent
    def videos_researcher(self) -> Agent:
        return Agent(
            config=self.agents_config['videos_researcher'],
            tools=[YouTubeSearchToolWrapper(), ScrapeWebsiteTool()],
        )

    @agent
    def google_researcher(self) -> Agent:
        return Agent(
            config=self.agents_config['google_researcher'],
            # tools=[SerperDevTool()],
        )

    @agent
    def wikipedia_researcher(self) -> Agent:
        return Agent(
            config=self.agents_config['wikipedia_researcher'],
            tools=[WikipediaSearchToolWrapper()],
        )

    @agent
    def comedian_agent(self) -> Agent:
        return Agent(
            config=self.agents_config['comedian'],
        )

    @task
    def fetch_videos_information(self) -> Task:
        return Task(
            config=self.tasks_config['fetch_videos_information'],
            agent=self.videos_researcher(),
            output_pydantic=VideosInformation,
            async_execution=True,
        )

    @task
    def lookup_in_google(self) -> Task:
        return Task(
            config=self.tasks_config['research_channel'],
            agent=self.google_researcher(),
            async_execution=True
        )

    @task
    def lookup_in_wikipedia(self) -> Task:
        return Task(
            config=self.tasks_config['lookup_in_wikipedia'],
            agent=self.wikipedia_researcher(),
            async_execution=True
        )

    @task
    def create_joke_task(self) -> Task:
        return Task(
            config=self.tasks_config['create_joke'],
            agent=self.comedian_agent(),
            output_pydantic=JokeWithExplanation,
            context=[self.fetch_videos_information(), self.lookup_in_google(), self.lookup_in_wikipedia()],
        )

    @crew
    def crew(self) -> Crew:
        return Crew(
            agents=self.agents,
            tasks=self.tasks,
            verbose=True,
        )
