import sys
from pathlib import Path

current_dir = Path(__file__).resolve().parent
target_dir = current_dir.parent.parent

sys.path.append(str(target_dir))

from src.utils.config import load_config
from src.utils.spark_session import get_spark_session

from src.embeddings.embedder import Embedder

from src.vector_search.faiss_index import (
    FaissIndex
)

from src.retrieval.semantic_retriever import (
    SemanticRetriever
)

config = load_config()

spark = get_spark_session()

embedder = Embedder(config)

df = spark.sql("""
SELECT *
FROM workspace.memory.semantic_memory
""")

rows = df.collect()

embeddings = []
documents = []

for row in rows:

    embeddings.append(row["embedding"])

    documents.append({
        "doc_id": row["doc_id"],
        "content": row["content"]
    })

dimension = len(embeddings[0])

vector_index = FaissIndex(dimension)

vector_index.add_embeddings(
    embeddings,
    documents
)

retriever = SemanticRetriever(
    embedder,
    vector_index
)

results = retriever.retrieve(
    "What electronics did customer buy?"
)

print(results)