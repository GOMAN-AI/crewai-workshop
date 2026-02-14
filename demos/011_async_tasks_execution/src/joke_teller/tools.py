from crewai.tools import BaseTool
from typing import Type
from pydantic import BaseModel, Field
from langchain_community.tools import YouTubeSearchTool, WikipediaQueryRun
from langchain_community.utilities import WikipediaAPIWrapper


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

class WikipediaSearchToolWrapperSchema(BaseModel):
    query: str = Field(..., description="The query to search for on Wikipedia.")

class WikipediaSearchToolWrapper(BaseTool):
    name: str = "Wikipedia Search"
    description: str = "Search for information on Wikipedia"
    search: WikipediaQueryRun = Field(default_factory=lambda: WikipediaQueryRun(api_wrapper=WikipediaAPIWrapper()))
    args_schema: Type[BaseModel] = WikipediaSearchToolWrapperSchema

    def _run(self, query: str) -> str:
        """Execute the Wikipedia search query and return results"""
        try:
            return self.search.run(query)
        except Exception as e:
            return f"Error performing Wikipedia search: {str(e)}"
