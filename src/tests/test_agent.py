from src.agent import Agent

def test_agent():

    agent = Agent()

    result = agent.answer(
        "policy"
    )

    assert "response" in result
