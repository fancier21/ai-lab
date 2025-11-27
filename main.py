import os
import time
from typing import TypedDict

from dotenv import load_dotenv
from langchain.chat_models import init_chat_model
from langgraph.graph import END, START, MessagesState, StateGraph

load_dotenv()

# llm = init_chat_model(
#     model="gpt-5-nano",
#     api_key=os.getenv("OPENAI_API_KEY"),
#     base_url=os.getenv("OPENAI_BASE_URL"),
#     organization=os.getenv("OPENAI_ORGANIZATION"),
# )

# response = llm.invoke("Write a one-sentence bedtime story about a unicorn.")
# print(response)


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
    return {"greeting": greeting}  # Replace ___ with "greeting"


# TODO 2: Complete the enhance_node function
# Hint: Add "How are you?" to the existing greeting
def enhance_node(state: State):
    """A node that enhances the greeting"""
    print("  🔄 Processing in enhance_node...")
    time.sleep(2)  # Simulate processing time - helps visualize flow
    enhanced = state["greeting"] + " How are you?"
    return {"greeting": enhanced}  # Replace ___ with enhanced


# NOW we build a graph!
print("Building your first graph:\n")

# TODO 1: Create a StateGraph with our State
# Hint: StateGraph takes State as parameter
workflow = StateGraph(State)  # Replace ___ with StateGraph

# TODO 2: Add nodes to the graph
# Hint: Use add_node method
workflow.add_node("greet", greet_node)
workflow.add_node("enhance", enhance_node)  # Replace ___ with add_node

# TODO 3: Connect nodes with edges
# Hint: The flow should be: START → greet → enhance → END
workflow.set_entry_point("greet")
workflow.add_edge("greet", "enhance")  # Replace ___ with "enhance"
workflow.add_edge("enhance", END)

# Compile the graph
print("Compiling graph...")
app = workflow.compile()
print("✅ Graph compiled successfully!\n")

# Run the graph!
print("Running the graph:")
result = app.invoke({"name": "Bob", "greeting": ""})

print(f"\nFinal result: {result}")


def main():
    print("Hello from ai-lab!")


if __name__ == "__main__":
    main()
