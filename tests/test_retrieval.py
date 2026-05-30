from src.retrieval import Retriever

def test_retrieve():

    r = Retriever()

    result = r.retrieve(
        "query"
    )

    assert len(result) > 0
