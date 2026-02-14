from crewai import Agent, Crew, Task
from crewai.project import CrewBase, agent, crew, task
from shared.llm import LMSTUDIO_QWEN_2_5_7B_LLM
from joke_with_explanation import JokeWithExplanation

@CrewBase
class CreateJokeCrew():
    @agent
    def comedian_agent(self) -> Agent:
        return Agent(
            llm=LMSTUDIO_QWEN_2_5_7B_LLM,
            config=self.agents_config['comedian'],
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
