"""Felix through LangChain and LangGraph.

pip install langchain-mcp-adapters langgraph "langchain[openai]"
export FELIX_API_KEY=fk_...   OPENAI_API_KEY=sk-...
python agent.py
"""
import asyncio
import os

from langchain_mcp_adapters.client import MultiServerMCPClient
from langgraph.prebuilt import create_react_agent


async def main() -> None:
    client = MultiServerMCPClient({
        "felix": {
            "transport": "streamable_http",
            "url": "https://mcp.felix.trade/mcp",
            "headers": {"Authorization": f"Bearer {os.environ['FELIX_API_KEY']}"},
        }
    })
    tools = await client.get_tools()
    agent = create_react_agent("openai:gpt-4.1", tools)
    result = await agent.ainvoke({"messages": "Quote BTC and preview a $50 long. Do not place it."})
    print(result["messages"][-1].content)


asyncio.run(main())
