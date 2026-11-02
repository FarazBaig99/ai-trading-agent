from langchain_huggingface import HuggingFaceEmbeddings
from langchain_community.vectorstores import Chroma

DB_DIR = "chroma_db"

def query_brain(question: str):
    print("AI Brain se strategies search ki ja rahi hain...")
    embeddings = HuggingFaceEmbeddings(model_name="all-MiniLM-L6-v2")
    vector_db = Chroma(persist_directory=DB_DIR, embedding_function=embeddings)

    # Top 3 matching strategies nikalna
    results = vector_db.similarity_search(question, k=3)
    
    print(f"\n🔍 Sawal: {question}\n" + "="*60)
    for i, doc in enumerate(results, 1):
        source = doc.metadata.get('source', 'Unknown')
        print(f"\n[Source {i}]: {source}")
        print(doc.page_content.strip()[:350] + "...\n" + "-"*40)

if __name__ == "__main__":
    # Test ke liye Candlestick ya RSI ka koi sawal poochte hain
    query_brain("What are the key rules for candlestick confirmation or risk management?")