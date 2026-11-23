"""Felix through LangChain and LangGraph.

pip install langchain-mcp-adapters langgraph "langchain[openai]"
export FELIX_API_KEY=fk_...   OPENAI_API_KEY=sk-...
python agent.py
"""
import asyncio
import os

from langchain_mcp_adapters.client import MultiServerMCPClient
from langgraph.prebuilt import create_react_agent

# Read and preview tools only. This agent can't place orders or move money.
# Add order tools only behind your own approval step and a key with tight limits.
READ_ONLY = {"get_status", "search_markets", "get_quote", "get_orderbook", "research_market", "preview_order"}


async def main() -> None:
    client = MultiServerMCPClient({
        "felix": {
            "transport": "streamable_http",
            "url": "https://mcp.felix.trade/mcp",
            "headers": {"Authorization": f"Bearer {os.environ['FELIX_API_KEY']}"},
        }
    })
    tools = [tool for tool in await client.get_tools() if tool.name in READ_ONLY]
    agent = create_react_agent("openai:gpt-4.1", tools)
    result = await agent.ainvoke({"messages": "Quote BTC and preview a $50 long."})
    print(result["messages"][-1].content)


asyncio.run(main())
