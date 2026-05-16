import sys
from pathlib import Path

current_dir = Path(__file__).resolve().parent
target_dir = current_dir.parent.parent

sys.path.append(str(target_dir))

from src.utils.config import load_config

from src.embeddings.embedder import Embedder

from src.vector_search.databricks_vector_search import (
    DatabricksVectorSearch
)

from src.retrieval.databricks_semantic_retriever import (
    DatabricksSemanticRetriever
)

config = load_config()

embedder = Embedder(config)

vector_search = DatabricksVectorSearch(
    endpoint_name=config["vector_search"]["endpoint_name"],
    index_name=config["vector_search"]["index_name"]
)

retriever = DatabricksSemanticRetriever(
    embedder,
    vector_search
)

results = retriever.retrieve(
    "What electronics products did customer purchase?"
)

print(results)