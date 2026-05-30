class Retriever:

    def __init__(self):
        self.documents = [
            "AWS Lambda processes incoming events",
            "SQS provides message queuing",
            "DynamoDB stores application data",
            "Claude API generates responses"
        ]

    def retrieve(self, query):

        results = []

        for doc in self.documents:
            if query.lower() in doc.lower():
                results.append(doc)

        return results if results else ["No matching documents found"]
