from phi.agent import Agent
from phi.model.google import Gemini
from phi.tools.yfinance import YFinanceTools

# Set your Gemini API key here
gemini_api_key = "AIzaSyAlyXEQc7aWeWcyZXiHDJ4EJeyynzovd-M"  # Replace with your actual Gemini API key

finance_agent = Agent(
    name="Finance Agent",
    model=Gemini(
        id="gemini-1.5-flash",
        api_key=gemini_api_key  # Pass the API key directly to the Gemini model
    ),
    tools=[YFinanceTools(stock_price=True, analyst_recommendations=True, company_info=True, company_news=True)],
    instructions=["Use tables to display data"],
    show_tool_calls=True,
    markdown=True,
)

finance_agent.print_response("Summarize analyst recommendations for NVDA", stream=True)
