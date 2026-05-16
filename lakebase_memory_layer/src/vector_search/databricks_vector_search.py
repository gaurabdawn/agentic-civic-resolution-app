from databricks.vector_search.client import (
    VectorSearchClient
)

class DatabricksVectorSearch:

    def __init__(
        self,
        endpoint_name,
        index_name
    ):

        self.client = VectorSearchClient()

        self.index = self.client.get_index(
            endpoint_name=endpoint_name,
            index_name=index_name
        )

    def similarity_search(
        self,
        query_embedding,
        columns,
        num_results=3
    ):

        results = self.index.similarity_search(
            query_vector=query_embedding,
            columns=columns,
            num_results=num_results
        )

        return results