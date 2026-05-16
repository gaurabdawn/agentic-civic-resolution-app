import sys
from pathlib import Path

current_dir = Path(__file__).resolve().parent
target_dir = current_dir.parent.parent

sys.path.append(str(target_dir))


from src.utils.config import load_config
from src.embeddings.embedder import Embedder

config = load_config()

embedder = Embedder(config)

embedding = embedder.generate_embedding(
    "customer purchased laptop"
)

print(type(embedding))
print(len(embedding))
print(embedding[:10])