from sentence_transformers import SentenceTransformer

class Embedder:

    def __init__(self, config):

        self.model_name = (
            config["embedding"]["model_name"]
        )

        self.model = SentenceTransformer(
            self.model_name
        )

    def generate_embedding(self, text):

        embedding = self.model.encode(text)

        return embedding.tolist()