from llama_index.core import VectorStoreIndex, SimpleDirectoryReader
from llama_index.llms.ollama import Ollama

def execute_test_query(llm):
    documents = SimpleDirectoryReader("./notes.txt").load_data()
    index = VectorStoreIndex.from_documents(documents, llm=llm)

    query_engine = index.as_query_engine(llm=llm)

    response = query_engine.query("Summarise this content")
    print(response)

def __main__():
    llm = Ollama(model="mistral")
    execute_test_query(llm)

if __name__ == "__main__":
    __main__()