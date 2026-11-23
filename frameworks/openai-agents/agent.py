"""Felix through the OpenAI Agents SDK.

pip install openai-agents
export FELIX_API_KEY=fk_...   OPENAI_API_KEY=sk-...
python agent.py
"""
import asyncio
import os

from agents import Agent, Runner
from agents.mcp import MCPServerStreamableHttp, create_static_tool_filter

# Read and preview tools only. This agent can't place orders or move money.
# Add order tools only behind your own approval step and a key with tight limits.
READ_ONLY = ["get_status", "search_markets", "get_quote", "get_orderbook", "research_market", "preview_order"]


async def main() -> None:
    async with MCPServerStreamableHttp(
        name="felix",
        tool_filter=create_static_tool_filter(allowed_tool_names=READ_ONLY),
        params={
            "url": "https://mcp.felix.trade/mcp",
            "headers": {"Authorization": f"Bearer {os.environ['FELIX_API_KEY']}"},
        },
    ) as felix:
        agent = Agent(
            name="Trader",
            instructions="Use Felix to research markets and preview trades.",
            mcp_servers=[felix],
        )
        result = await Runner.run(agent, "Quote BTC and preview a $50 long.")
        print(result.final_output)


asyncio.run(main())
