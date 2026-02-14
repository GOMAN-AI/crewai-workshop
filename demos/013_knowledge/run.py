from breweries_crew.crew import BreweriesCrew
from shared.tracing import traceable
from crewai.knowledge.source.json_knowledge_source import JSONKnowledgeSource

@traceable
def main():
    crew = BreweriesCrew().crew()
    inputs = { "location": "Portugal" }
    result = crew.kickoff(inputs=inputs)
    print("\nBrewery Research Results:")
    print(result)

if __name__ == '__main__':
    main()
