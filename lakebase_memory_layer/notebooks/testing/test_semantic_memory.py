import sys
from pathlib import Path

current_dir = Path(__file__).resolve().parent
target_dir = current_dir.parent.parent

sys.path.append(str(target_dir))

from src.utils.config import load_config
from src.utils.spark_session import get_spark_session

from src.embeddings.embedder import Embedder

from src.memory.semantic_memory_manager import (
    SemanticMemoryManager
)

config = load_config()

spark = get_spark_session()

embedder = Embedder(config)

semantic_manager = SemanticMemoryManager(
    spark=spark,
    config=config,
    embedder=embedder
)

semantic_manager.store_memory(
    id="doc_1",
    content="Customer purchased gaming laptop"
)

semantic_manager.store_memory(
    id="doc_2",
    content="Customer ordered Apple iPhone"
)