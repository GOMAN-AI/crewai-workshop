from crewai import Agent, Crew, Task, Process
from crewai.project import CrewBase, agent, crew, task
from .tools import WeatherForecastTool, WikipediaSearchToolWrapper
from crewai_tools import SerperDevTool
from crewai.knowledge.source.json_knowledge_source import JSONKnowledgeSource
from shared.llm import OPENAI_O4_MINI_LLM

user_json = JSONKnowledgeSource(
  file_paths=["user.json"]
)

@CrewBase
class PersonalAssistantCrew():
    @agent
    def comedian_agent(self) -> Agent:
        return Agent(
            config=self.agents_config['comedian'],
        )

    @agent
    def google_researcher(self) -> Agent:
        return Agent(
            config=self.agents_config['google_researcher'],
            reasoning=True,
            tools=[SerperDevTool()],
        )

    @agent
    def wikipedia_researcher(self) -> Agent:
        return Agent(
            config=self.agents_config['wikipedia_researcher'],
            tools=[WikipediaSearchToolWrapper()],
        )

    @agent
    def forecaster_agent(self) -> Agent:
        return Agent(
            config=self.agents_config['forecaster'],
            knowledge_sources=[user_json],
            tools=[WeatherForecastTool()],
        )

    @task
    def process_user_request(self) -> Task:
        return Task(
            config=self.tasks_config['process_user_request']
        )

    @crew
    def crew(self) -> Crew:
        return Crew(
            agents=self.agents,
            tasks=self.tasks,
            verbose=True,
            process=Process.hierarchical,
            manager_llm=OPENAI_O4_MINI_LLM,
            manager_agent=None,
        )
