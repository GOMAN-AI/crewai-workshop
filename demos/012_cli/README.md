# Commands to demo

```
crewai create crew comedy_crew
crewai run
crewai train -n 3 -f jokes.pkl
crewai log-tasks-outputs
crewai test -n 3 -m gpt-4o
crewai chat
```

# Cursor prompt to generate

```
I want you to rework this boilerplate project.
It should have only one task and one agent.
One agent will be the comedy agent - his backstory will be in the comedy and about making jokes
Task will be to make a single joke on a specific topic.
Please create these descriptions and all necessary fields following the same pattern as you see on the comedy crew here.
```
