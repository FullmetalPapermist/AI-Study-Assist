from llama_index.core import VectorStoreIndex, SimpleDirectoryReader, Settings
from llama_index.llms.ollama import Ollama
from llama_index.embeddings.huggingface import HuggingFaceEmbedding
from llama_index.core.node_parser import SimpleNodeParser
from llama_index.core.response_synthesizers import ResponseMode



def init_query_engine():
    parser = SimpleNodeParser.from_defaults(chunk_size=512)

    llm = Ollama(model="mistral")
    embed_model = HuggingFaceEmbedding(model_name="sentence-transformers/all-MiniLM-L6-v2")
    Settings.llm = llm
    Settings.embed_model = embed_model
    documents = SimpleDirectoryReader("./notes").load_data()

    index = VectorStoreIndex.from_documents(
        documents,
        llm=llm,
        embed_model=embed_model,
        request_timeout=3000,
        node_parser=parser
    )
    query_engine = index.as_query_engine(response_mode=ResponseMode.COMPACT)


    return query_engine
