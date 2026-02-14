import os
from textwrap import dedent
from crewai import Agent, Task, Crew


def get_mcp_server_params():
    """Get MCP server parameters for GitHub Issues API."""
    github_token = os.environ.get("GITHUB_PERSONAL_ACCESS_TOKEN")

    if not github_token:
        raise ValueError("GITHUB_PERSONAL_ACCESS_TOKEN environment variable required")

    return {
        "url": "https://api.githubcopilot.com/mcp/x/issues/readonly",
        "transport": "streamable-http",
        "headers": {"Authorization": f"Bearer {github_token}"},
    }


def create_issue_counter_crew(tools, repo: str) -> Crew:
    """Create a CrewAI crew to count GitHub issues."""

    github_analyst = Agent(
        role="GitHub Issue Analyst",
        goal="Count open issues in GitHub repositories accurately",
        backstory=dedent("""
            You are an expert at analyzing GitHub repositories.
            You use the available GitHub tools to fetch issue data
            and provide accurate counts of open issues.
        """),
        tools=tools,
        verbose=True
    )

    count_issues_task = Task(
        description=dedent(f"""
            Count the total number of open issues in the repository: {repo}

            Use the available GitHub tools to:
            1. List or search for open issues in the repository
            2. Count them accurately
            3. Report the final count

            Be precise and report the exact number found.
        """),
        expected_output="The count of open issues in the repository",
        agent=github_analyst
    )

    return Crew(
        agents=[github_analyst],
        tasks=[count_issues_task],
        verbose=True
    )
