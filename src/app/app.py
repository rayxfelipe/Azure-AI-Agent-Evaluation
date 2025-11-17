
# Minimal demo endpoint (no external calls). Replace with Foundry agent.
from dataclasses import dataclass

@dataclass
class DemoAgent:
    def answer(self, question: str, context: str | None = None) -> str:
        # Extremely naive: echo expected intent; replace with real agent call.
        return f"(demo) Based on policy/context, here is a compliant answer to: {question}"

agent = DemoAgent()

def respond(q: str, ctx: str | None = None) -> str:
    return agent.answer(q, ctx)
