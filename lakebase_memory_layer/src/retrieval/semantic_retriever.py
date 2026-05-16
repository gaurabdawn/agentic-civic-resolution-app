class SemanticRetriever:

    def __init__(
        self,
        embedder,
        vector_index
    ):

        self.embedder = embedder
        self.vector_index = vector_index

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

        results = self.vector_index.search(
            query_embedding,
            top_k=top_k
        )

        return results