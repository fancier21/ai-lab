#!/usr/bin/env python3
"""Task 2: Creating Nodes - Functions that will become graph nodes"""

import os
import time
from typing import TypedDict

# ┌─────────────────────────────────────────┐
# │  Understanding Nodes in LangGraph       │
# └─────────────────────────────────────────┘
#
#     ┌─────────────────┐
#     │  Initial State  │
#     │ name: "Alice"   │
#     │ greeting: ""    │
#     └────────┬────────┘
#              │
#              ▼
#     ┌─────────────────┐
#     │   greet_node    │ ← Node is a function
#     │  Takes state    │
#     │  Returns:       │
#     │  {greeting:...} │ ← Partial update
#     └────────┬────────┘
#              │ (LangGraph merges)
#              ▼
#     ┌─────────────────┐
#     │  Updated State  │
#     │ name: "Alice"   │ ← Unchanged
#     │ greeting:"Hello"│ ← Updated
#     └────────┬────────┘
#              │
#              ▼
#     ┌─────────────────┐
#     │  enhance_node   │ ← Another function
#     │  Takes state    │
#     │  Returns:       │
#     │  {greeting:...} │ ← Another update
#     └────────┬────────┘
#              │
#              ▼
#     ┌─────────────────┐
#     │   Final State   │
#     │ name: "Alice"   │
#     │ greeting:"Hello │
#     │  ...How are you?"│
#     └─────────────────┘
#
# KEY INSIGHT: Nodes are just functions!
# - Take state as input
# - Return partial updates
# - LangGraph handles merging

print("🔷 Task 2: Creating Your First Node\n")


# Define our state structure
class State(TypedDict):
    name: str
    greeting: str


# TODO 1: Complete the greet_node function
# Hint: Return a dictionary with "greeting" key
def greet_node(state: State):
    """A node that creates a greeting from the name"""
    print("  🔄 Processing in greet_node...")
    time.sleep(2)  # Simulate processing time
    greeting = f"Hello, {state['name']}!"
    return {"___": greeting}  # Replace ___ with "greeting"


# TODO 2: Complete the enhance_node function
# Hint: Add "How are you?" to the existing greeting
def enhance_node(state: State):
    """A node that enhances the greeting"""
    print("  🔄 Processing in enhance_node...")
    time.sleep(2)  # Simulate processing time - helps visualize flow
    enhanced = state["greeting"] + " How are you?"
    return {"greeting": ___}  # Replace ___ with enhanced


# Test nodes directly (no graph needed yet!)
print("Testing nodes manually:\n")

# Start with initial state
initial_state = {"name": "Alice", "greeting": ""}
print(f"Initial state: {initial_state}")

# Call first node
print("\nCalling greet_node...")
update1 = greet_node(initial_state)
print(f"Node returned: {update1}")

# For manual testing, simulate what LangGraph does
state_after_greet = {"name": "Alice", "greeting": update1["greeting"]}
print(f"State after greet: {state_after_greet}")

# Call second node
print("\nCalling enhance_node...")
update2 = enhance_node(state_after_greet)
print(f"Node returned: {update2}")

# Final state after second node
final_state = {"name": "Alice", "greeting": update2["greeting"]}
print(f"Final state: {final_state}")

print("\n" + "=" * 60)
print("💡 KEY CONCEPTS:")
print("- Nodes are Python functions that take state and return updates")
print("- We're testing functions here WITHOUT a graph")
print("- In Task 3, we'll add these functions to a StateGraph")
print("- LangGraph will handle state merging automatically in a real graph")
print("=" * 60)

os.makedirs("/root/markers", exist_ok=True)
with open("/root/markers/task2_nodes_complete.txt", "w") as f:
    f.write("TASK2_COMPLETE")

print("\n✅ Task 2 completed!")
