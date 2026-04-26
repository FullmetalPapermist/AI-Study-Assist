from llama_index.core import VectorStoreIndex, SimpleDirectoryReader

def execute_test_query():
    documents = SimpleDirectoryReader("./notes.txt").load_data()
    index = VectorStoreIndex.from_documents(documents)

    query_engine = index.as_query_engine()

    response = query_engine.query("Summarise this content")
    print(response)

def __main__():
    execute_test_query()