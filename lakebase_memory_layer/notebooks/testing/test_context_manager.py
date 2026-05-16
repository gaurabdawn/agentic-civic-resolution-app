import sys
from pathlib import Path

current_dir = Path(__file__).resolve().parent
target_dir = current_dir.parent.parent

sys.path.append(str(target_dir))

from src.utils.config import load_config
from src.utils.spark_session import get_spark_session

from src.embeddings.embedder import Embedder

from src.memory.session_memory_manager import (
    SessionMemoryManager
)

from src.vector_search.faiss_index import (
    FaissIndex
)

from src.retrieval.semantic_retriever import (
    SemanticRetriever
)

from src.memory.context_manager import (
    ContextManager
)

config = load_config()

spark = get_spark_session()

embedder = Embedder(config)

session_manager = SessionMemoryManager(
    spark,
    config
)

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

context_manager = ContextManager(
    session_manager,
    retriever
)

context = context_manager.build_context(
    user_id="u1",
    query="What electronics did customer buy?"
)

print(context)