from crewai import Agent, Crew, Task
from crewai.project import CrewBase, agent, crew, task
from crewai.knowledge.source.json_knowledge_source import JSONKnowledgeSource
from crewai_tools import JSONSearchTool

json_breweries = JSONKnowledgeSource(
  file_paths=["customize.json"]
)

search_tool = JSONSearchTool(json_path='knowledge/breweries.json')

@CrewBase
class BreweriesCrew():
    @agent
    def brewery_researcher(self) -> Agent:
        return Agent(
            config=self.agents_config['brewery_researcher'],
            knowledge_sources=[json_breweries],
            tools=[search_tool]
        )

    @task
    def research_breweries_task(self) -> Task:
        return Task(
            config=self.tasks_config['research_breweries'],
        )

    @crew
    def crew(self) -> Crew:
        return Crew(
            agents=self.agents,
            tasks=self.tasks,
            verbose=True
        )
