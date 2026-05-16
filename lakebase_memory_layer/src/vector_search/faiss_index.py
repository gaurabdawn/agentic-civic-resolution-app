import faiss
import numpy as np

class FaissIndex:

    def __init__(self, dimension):

        self.dimension = dimension

        self.index = faiss.IndexFlatL2(
            dimension
        )

        self.documents = []

    def add_embeddings(
        self,
        embeddings,
        documents
    ):

        vectors = np.array(
            embeddings
        ).astype("float32")

        self.index.add(vectors)

        self.documents.extend(documents)

    def search(
        self,
        query_embedding,
        top_k=3
    ):

        query_vector = np.array(
            [query_embedding]
        ).astype("float32")

        distances, indices = self.index.search(
            query_vector,
            top_k
        )

        results = []

        for idx in indices[0]:

            results.append(
                self.documents[idx]
            )

        return results