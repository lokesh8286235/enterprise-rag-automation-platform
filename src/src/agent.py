from src.retrieval import Retriever

class Agent:

    def __init__(self):
        self.retriever = Retriever()

    def answer(self, query):

        context = self.retriever.retrieve(query)

        return {
            "query": query,
            "context": context,
            "response": "Claude generated response"
        }
