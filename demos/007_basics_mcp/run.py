# Import traceable first to ensure instrumentation is set up before other imports
from shared.tracing import traceable

import re
from crewai_tools import MCPServerAdapter
from github_issues import get_mcp_server_params, create_issue_counter_crew


def validate_repo(repo: str) -> bool:
    return bool(re.match(r"^[a-zA-Z0-9_.-]+/[a-zA-Z0-9_.-]+$", repo))


@traceable
def main():
    print("=" * 60)
    print("GitHub Issues Counter (MCP + CrewAI Edition)")
    print("=" * 60)
    print()

    repo = input("Enter a GitHub repository (e.g., facebook/react): ").strip()
    if not validate_repo(repo):
        print("Error: Invalid format. Use 'owner/repo'")
        return

    print(f"\nCounting open issues for {repo}...\n")

    server_params = get_mcp_server_params()

    with MCPServerAdapter(server_params) as tools:
        print(f"Available tools: {[tool.name for tool in tools]}")

        crew = create_issue_counter_crew(tools, repo)
        result = crew.kickoff()

        print("=" * 60)
        print("RESULT")
        print("=" * 60)
        print(result.raw)


if __name__ == "__main__":
    main()
