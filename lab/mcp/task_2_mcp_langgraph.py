#!/usr/bin/env python3
"""Task 2: MCP and LangGraph Integration - Connecting MCP servers to agents"""

import asyncio
import os
from typing import TypedDict

from langchain_openai import ChatOpenAI
from langgraph.prebuilt import create_react_agent

# ╔════════════════════════════════════════╗
# ║   MCP + LangGraph Integration Flow     ║
# ╚════════════════════════════════════════╝
#
#        [User Query]
#             │
#             ▼
#     ┌───────────────┐
#     │ LangGraph     │
#     │ React Agent   │
#     └───────┬───────┘
#             │
#       ┌─────┴─────┐
#       │MCP Client │
#       └─────┬─────┘
#             │
#       ┌─────┴─────┐
#       ▼           ▼
# ┌──────────┐ ┌─────────┐
# │MCP Server│ │   LLM   │
# │Calculator│ │Response │
# │   🔢     │ │   💬    │
# └──────────┘ └─────────┘
#
# MCP Tool Naming Convention:
# When tools are loaded, they follow pattern:
# Original: add, multiply
# In Agent: Automatically handled by MCP adapter

print("🔌 Task 2: MCP and LangGraph Integration\n")

# Import MCP adapter components
try:
    from langchain_mcp_adapters.client import MultiServerMCPClient
except ImportError:
    print(
        "⚠️ Creating mock MCP client for learning (install 'pip install langchain-mcp-adapters' for real)"
    )

    # Mock implementation for learning
    class MultiServerMCPClient:
        def __init__(self, servers):
            self.servers = servers

        async def get_tools(self):
            """Mock tools from calculator server"""

            def mock_add(a: float, b: float) -> float:
                """Add two numbers"""
                return a + b

            def mock_multiply(a: float, b: float) -> float:
                """Multiply two numbers"""
                return a * b

            # Return mock tools
            return [mock_add, mock_multiply]


# Initialize the LLM
model = ChatOpenAI(
    model=os.getenv("OPENAI_MODEL", "openai/gpt-4.1-mini"),
    base_url=os.getenv("OPENAI_API_BASE"),
    api_key=os.getenv("OPENAI_API_KEY"),
    temperature=0,
)

print("Building MCP-integrated agent:\n")

# TODO 1: Initialize MultiServerMCPClient
# Hint: Configure calculator server with stdio transport
client = MultiServerMCPClient(
    {
        ___: {  # Replace ___ with "calculator"
            "command": "python",
            # In production, use full path to your server
            "args": ["/root/code/task_1_mcp_basics.py"],
            "transport": "stdio",
        }
    }
)


async def run_agent_with_mcp():
    """Create and run agent with MCP tools"""

    # TODO 2: Get tools from MCP client
    # Hint: Call client.get_tools()
    tools = await ___  # Replace ___ with client.get_tools()

    # TODO 3: Create react agent with tools
    # Hint: Use create_react_agent with model and tools
    agent = ___(model, tools)  # Replace ___ with create_react_agent

    print("✅ Agent created with MCP tools!\n")
    print("=" * 60)
    print("TESTING MCP-INTEGRATED AGENT:")
    print("=" * 60)

    # Test 1: Math query (should use MCP tools)
    print("\nTest 1: Math Query")
    math_response = await agent.ainvoke({"messages": "What is 25 plus 17?"})
    print(f"Response: {math_response['messages'][-1].content}")

    # Test 2: Another math query
    print("\nTest 2: Multiplication Query")
    multiply_response = await agent.ainvoke({"messages": "Calculate 8 times 9"})
    print(f"Response: {multiply_response['messages'][-1].content}")

    # Test 3: Complex math
    print("\nTest 3: Complex Math")
    complex_response = await agent.ainvoke({"messages": "What's (3 + 5) x 12?"})
    print(f"Response: {complex_response['messages'][-1].content}")

    # Test 4: Non-math query
    print("\nTest 4: Non-Math Query")
    general_response = await agent.ainvoke(
        {"messages": "What is the capital of France?"}
    )
    print(f"Response: {general_response['messages'][-1].content}")


# Run the agent
if __name__ == "__main__":
    print("Starting MCP + LangGraph integration...")

    # Run async function
    asyncio.run(run_agent_with_mcp())

    print("\n" + "=" * 60)
    print("💡 KEY CONCEPTS:")
    print("- MultiServerMCPClient connects to MCP servers")
    print("- client.get_tools() loads tools from servers")
    print("- create_react_agent builds agent with tools")
    print("- Agent automatically routes to appropriate tools")
    print("- MCP handles tool execution transparently")
    print("=" * 60)

    # Create marker file
    os.makedirs("/root/markers", exist_ok=True)
    with open("/root/markers/task2_integration_complete.txt", "w") as f:
        f.write("TASK2_COMPLETE")
