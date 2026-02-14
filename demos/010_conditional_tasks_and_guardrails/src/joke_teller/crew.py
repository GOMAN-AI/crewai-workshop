from crewai import Agent, Crew, Task
from crewai.project import CrewBase, agent, crew, task
from joke_with_explanation import JokeWithExplanation
from videos_information import VideosInformation
from .tools import YouTubeSearchToolWrapper
from crewai.tasks.task_output import TaskOutput
from crewai.tasks.conditional_task import ConditionalTask
from crewai_tools import SerperDevTool, ScrapeWebsiteTool
from typing import Any, Dict, List, Tuple, Union

PHRASES_INDICATING_THAN_SOMETHING_IS_WRONG_REGEXP = [
        "Copyright",
        "Privacy Policy",
        "Before you continue to YouTube",
        "Short Video",
        "Long Video",
]

def not_enough_information(output: TaskOutput) -> bool:
    information = output.pydantic
    if len(information.videos) < 3:
        return True
    return False

def validate_videos_information_correct(output: TaskOutput) -> Tuple[bool, Any]:
    information = output.pydantic
    if information is None:
        return (False, {"error": "Failed to parse output into structured format", "code": "PARSE_ERROR"})
    videos = information.videos

    if not videos:
        return (False, {"error": "Empty result", "code": "EMPTY_INPUT"})

    filtered = []

    for video in videos:
        selected = True

        if not video.title:
            selected = False

        for phrase in PHRASES_INDICATING_THAN_SOMETHING_IS_WRONG_REGEXP:
            if phrase in video.title:
                selected = False
                break

        if selected:
            filtered.append(video)

    if not filtered:
        return (False, {"error": "Failed to parse any videos", "code": "EMPTY_INPUT"})

    return (True, VideosInformation(videos=filtered))


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
    def google_researcher(self) -> Agent:
        return Agent(
            config=self.agents_config['google_researcher'],
            tools=[SerperDevTool()],
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
            output_pydantic=VideosInformation,
            guardrail=validate_videos_information_correct,
        )

    @task
    def add_additiona_information(self) -> Task:
        return ConditionalTask(
            config=self.tasks_config['research_channel'],
            agent=self.google_researcher(),
            condition=not_enough_information,
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
