"""Felix through the OpenAI Agents SDK.

pip install openai-agents
export FELIX_API_KEY=fk_...   OPENAI_API_KEY=sk-...
python agent.py
"""
import asyncio
import os

from agents import Agent, Runner
from agents.mcp import MCPServerStreamableHttp


async def main() -> None:
    async with MCPServerStreamableHttp(
        name="felix",
        params={
            "url": "https://mcp.felix.trade/mcp",
            "headers": {"Authorization": f"Bearer {os.environ['FELIX_API_KEY']}"},
        },
    ) as felix:
        agent = Agent(
            name="Trader",
            instructions="Use Felix to research and preview trades. Never place an order unless asked.",
            mcp_servers=[felix],
        )
        result = await Runner.run(agent, "Quote BTC and preview a $50 long. Do not place it.")
        print(result.final_output)


asyncio.run(main())
