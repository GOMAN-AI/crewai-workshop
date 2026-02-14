from crewai import Agent, Crew, Task
from crewai.project import CrewBase, agent, crew, task
from crewai_tools import CodeInterpreterTool
import os

print(os.getenv('DOCKER_HOST'))

@CrewBase
class HeadsOrTailsCrew():
    @agent
    def game_generator_agent(self) -> Agent:
        return Agent(
            config=self.agents_config['game_generator'],
            allow_code_execution=True,
            tools=[CodeInterpreterTool()]
        )

    @agent
    def result_evaluator_agent(self) -> Agent:
        return Agent(
            config=self.agents_config['result_evaluator'],
        )

    @task
    def generate_result_task(self) -> Task:
        return Task(
            config=self.tasks_config['generate_result'],
            agent=self.game_generator_agent()
        )

    @task
    def evaluate_result_task(self) -> Task:
        return Task(
            config=self.tasks_config['evaluate_result'],
            agent=self.result_evaluator_agent(),
            context=[self.generate_result_task()]
        )

    @crew
    def crew(self) -> Crew:
        return Crew(
            agents=self.agents,
            tasks=self.tasks,
            verbose=True,
        )
