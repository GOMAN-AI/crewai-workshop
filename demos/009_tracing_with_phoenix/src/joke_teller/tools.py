from crewai.tools import BaseTool
from typing import Type
from pydantic import BaseModel, Field
from langchain_community.tools import YouTubeSearchTool

class YouTubeSearchToolWrapperSchema(BaseModel):
    query: str = Field(..., description="The query to search for.")
    number: int = Field(5, description="Number of videos to fetch")

class YouTubeSearchToolWrapper(BaseTool):
    name: str = "Search"
    description: str = "Search for videos on YouTube"
    search: YouTubeSearchTool = Field(default_factory=YouTubeSearchTool)
    args_schema: Type[BaseModel] = YouTubeSearchToolWrapperSchema

    def _run(self, query: str, number: int) -> str:
        """Execute the search query and return results"""
        try:
            search = f"{query}, {number}"
            return self.search.run(search)
        except Exception as e:
            return f"Error performing search: {str(e)}"
