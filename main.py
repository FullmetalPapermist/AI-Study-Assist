from llama_index.core import VectorStoreIndex, SimpleDirectoryReader, Settings
from llama_index.llms.ollama import Ollama
from llama_index.embeddings.huggingface import HuggingFaceEmbedding

def execute_test_query(llm, embed_model):
    documents = SimpleDirectoryReader("./notes").load_data()

    index = VectorStoreIndex.from_documents(
        documents,
        llm=llm,
        embed_model=embed_model,
        request_timeout=120.0
    )

    query_engine = index.as_query_engine()

    response = query_engine.query("Summarise this content")
    print(response)

def __main__():
    llm = Ollama(model="mistral")
    embed_model = HuggingFaceEmbedding(model_name="sentence-transformers/all-MiniLM-L6-v2")
    Settings.llm = llm
    Settings.embed_model = embed_model
    execute_test_query(llm, embed_model)

if __name__ == "__main__":
    __main__()