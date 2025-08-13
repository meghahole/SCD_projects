import os
from dotenv import load_dotenv
from langchain.embeddings import OpenAIEmbeddings
from langchain.vectorstores import FAISS
from langchain.llms import OpenAI
from langchain.chains import RetrievalQA
from langchain.document_loaders import TextLoader
from langchain.text_splitter import RecursiveCharacterTextSplitter

# Load API key from .env
load_dotenv()
openai_api_key = os.getenv("OPENAI_API_KEY")

# Load the document
loader = TextLoader("data/knowledge.txt")
documents = loader.load()

# Split into chunks
text_splitter = RecursiveCharacterTextSplitter(chunk_size=500, chunk_overlap=50)
chunks = text_splitter.split_documents(documents)

# Create vector store
embeddings = OpenAIEmbeddings(openai_api_key=openai_api_key)
vectorstore = FAISS.from_documents(chunks, embeddings)

# Set up retriever + LLM
retriever = vectorstore.as_retriever()
llm = OpenAI(temperature=0, openai_api_key=openai_api_key)
qa_chain = RetrievalQA.from_chain_type(llm=llm, retriever=retriever)

# Ask user for input
while True:
    query = input("\nAsk a question (or type 'exit'): ")
    if query.lower() == 'exit':
        break
    answer = qa_chain.run(query)
    print(f"\nAnswer: {answer}")