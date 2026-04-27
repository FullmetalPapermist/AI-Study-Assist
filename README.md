# AI Study Assistant

A fully local Retrieval‑Augmented Generation (RAG) system built with:

- **Ollama (Mistral 7B)** for local LLM inference  
- **LlamaIndex** for document parsing, chunking, and semantic retrieval  
- **HuggingFace sentence‑transformer embeddings** for vector search  
- **Structured JSON workflows** for summarisation, question generation, answer evaluation, and adaptive feedback  

The assistant can summarise your notes, generate quiz questions, evaluate your answers, and adjust difficulty based on your performance — all running locally on your machine.

---

## Running the Application

From the project root:

```bash
python main.py

```
---

## HuggingFace Token (Highly recommended)
[HuggingFace](https://huggingface.co)

To set a token:

Linux/mac
```bash
export HF_TOKEN=your_token_here
```
Windows Powershell

```bash
setx HF_TOKEN your_token_here
```