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
    topic: str
    outline: str
    draft: str
    final: str


# Node 1: Create outline
def outline_node(state: State):
    """Creates an outline for the topic"""
    print("  🔄 Creating outline...")
    time.sleep(2)  # Visualize processing time
    outline = f"Outline for '{state['topic']}':\n1. Introduction\n2. Main Points\n3. Conclusion"
    return {"outline": outline}


# Node 2: Create draft
def draft_node(state: State):
    """Creates a draft based on the outline"""
    print("  🔄 Writing draft...")
    time.sleep(2)  # Visualize processing time
    draft = f"Draft: Expanding on the outline for '{state['topic']}'..."
    return {"draft": draft}


# TODO 1: Complete the review_node function
# Hint: Create final version and return {"final": ...}
def review_node(state: State):
    """Reviews and finalizes the content"""
    print("  🔄 Reviewing and finalizing...")
    time.sleep(2)  # Visualize processing time
    final = f"Final: Reviewed and polished content about '{state['topic']}'. Ready to publish!"
    return {"final": final}  # Replace ___ with "final"


print("Building multi-step workflow:\n")

# Build the complete workflow
workflow = StateGraph(State)

# TODO 2: Add all three nodes to the graph
# Hint: Use add_node for each node
workflow.add_node("outline", outline_node)
workflow.add_node("draft", draft_node)
workflow.add_node("review", review_node)

# TODO 3: Connect all nodes in sequence
# Hint: outline → draft → review → END
workflow.set_entry_point("outline")
workflow.add_edge("outline", "draft")
workflow.add_edge("draft", "review")
workflow.add_edge("review", END)

# Compile and run
app = workflow.compile()
print("Graph compiled! Running workflow...\n")

# Execute the complete flow
result = app.invoke(
    {"topic": "LangGraph Basics", "outline": "", "draft": "", "final": ""}
)

print("\n" + "=" * 60)
print("WORKFLOW RESULTS:")
print(f"Topic: {result['topic']}")
print(f"Outline: {result['outline']}")
print(f"Draft: {result['draft']}")
print(f"Final: {result['final']}")
print("=" * 60)


def main():
    print("Hello from ai-lab!")


if __name__ == "__main__":
    main()
