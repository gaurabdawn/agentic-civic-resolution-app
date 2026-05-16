class DatabricksSemanticRetriever:

    def __init__(
        self,
        embedder,
        vector_search
    ):

        self.embedder = embedder
        self.vector_search = vector_search

    def retrieve(
        self,
        query,
        top_k=3
    ):

        query_embedding = (
            self.embedder.generate_embedding(
                query
            )
        )

        results = (
            self.vector_search
            .similarity_search(
                query_embedding=query_embedding,
                columns=[
                    "doc_id",
                    "content"
                ],
                num_results=top_k
            )
        )

        return results