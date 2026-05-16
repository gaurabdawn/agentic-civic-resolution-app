class ContextManager:

    def __init__(
        self,
        session_memory_manager,
        semantic_retriever
    ):

        self.session_memory_manager = (
            session_memory_manager
        )

        self.semantic_retriever = (
            semantic_retriever
        )

    def build_context(
        self,
        user_id,
        query
    ):

        session_memory = (
            self.session_memory_manager
            .retrieve_memory(user_id)
            .collect()
        )

        semantic_memory = (
            self.semantic_retriever
            .retrieve(query)
        )

        context = {
            "session_memory": session_memory,
            "semantic_memory": semantic_memory
        }

        return context