import os
os.environ["GOOGLE_API_KEY"] = YOUR_GEMINI_API_KEY_HERE  # Replace with your actual Gemini API key
from phi.agent import Agent
from phi.model.google import Gemini  # Changed from OpenAIChat to Gemini
from phi.tools.duckduckgo import DuckDuckGo
from phi.tools.yfinance import YFinanceTools

web_agent = Agent(
    name="Web Agent",
    role="Search the web for information",
    model=Gemini(id="gemini-1.5-flash"),  # Changed from gpt-4o to gemini model
    tools=[DuckDuckGo()],
    instructions=["Always include sources"],
    show_tool_calls=True,
    markdown=True,
)

finance_agent = Agent(
    name="Finance Agent",
    role="Get financial data",
    model=Gemini(id="gemini-1.5-flash"), 
    tools=[YFinanceTools(stock_price=True, analyst_recommendations=True, company_info=True)],
    instructions=["Use tables to display data"],
    show_tool_calls=True,
    markdown=True,
)

# For the agent_team, we need to specify a model as well
agent_team = Agent(
    team=[web_agent, finance_agent],
    model=Gemini(id="gemini-1.5-flash"),  # Added Gemini model here
    instructions=["Always include sources", "Use tables to display data"],
    show_tool_calls=True,
    markdown=True,
)

agent_team.print_response("Summarize analyst recommendations and share the latest news for NVDA", stream=True)
