from langchain_community.document_loaders import TextLoader
from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain_huggingface import HuggingFaceEmbeddings
from langchain_community.vectorstores import FAISS

print("Loading FAQ document...")

# Load the FAQ document
loader = TextLoader("company_faq.txt", encoding="utf-8")
documents = loader.load()

print("Splitting document into chunks...")

# Split into chunks
text_splitter = RecursiveCharacterTextSplitter(
    chunk_size=500,
    chunk_overlap=100
)

chunks = text_splitter.split_documents(documents)

print(f"Total Chunks Created: {len(chunks)}")

print("Generating embeddings...")

# Create embeddings
embeddings = HuggingFaceEmbeddings(
    model_name="sentence-transformers/all-MiniLM-L6-v2"
)

print("Creating FAISS vector store...")

# Create FAISS vector database
vectorstore = FAISS.from_documents(chunks, embeddings)

# Save locally
vectorstore.save_local("faiss_index")

print("===================================")
print("Vector Store Created Successfully!")
print("Saved inside: faiss_index/")
print("===================================")