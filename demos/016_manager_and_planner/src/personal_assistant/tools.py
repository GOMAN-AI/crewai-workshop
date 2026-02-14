from crewai.tools import BaseTool
from typing import Type
from pydantic import BaseModel, Field
from langchain_community.tools import WikipediaQueryRun
from langchain_community.utilities import OpenWeatherMapAPIWrapper, WikipediaAPIWrapper

class WeatherForecastToolSchema(BaseModel):
    location: str = Field(..., description="The city name to get weather forecast for.")

class WeatherForecastTool(BaseTool):
    name: str = "Weather Forecast"
    description: str = "Get current weather information for a specific location"
    weather_api: OpenWeatherMapAPIWrapper = Field(default_factory=OpenWeatherMapAPIWrapper)
    args_schema: Type[BaseModel] = WeatherForecastToolSchema

    def _run(self, location: str) -> str:
        """Get weather forecast for the specified location"""
        try:
            weather_data = self.weather_api.run(location)
            return weather_data
        except Exception as e:
            return f"Error getting weather forecast: {str(e)}"

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
