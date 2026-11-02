import os
from langchain_community.document_loaders import PyPDFDirectoryLoader, DirectoryLoader, TextLoader
from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain_huggingface import HuggingFaceEmbeddings
from langchain_community.vectorstores import Chroma

DOCS_DIR = "trading_books"
NOTES_DIR = "Notes"
DB_DIR = "chroma_db"

def build_vector_store():
    all_documents = []

    # 1. Trading books folder se PDFs load karein
    if os.path.exists(DOCS_DIR):
        print(f"1. '{DOCS_DIR}' folder se PDFs read ho rahi hain...")
        pdf_loader = PyPDFDirectoryLoader(DOCS_DIR)
        pdf_docs = pdf_loader.load()
        all_documents.extend(pdf_docs)
        print(f"   -> {len(pdf_docs)} PDF pages load ho gaye.")
    else:
        print(f"'{DOCS_DIR}' folder nahi mila.")

    # 2. Notes folder se .md files load karein
    if os.path.exists(NOTES_DIR):
        print(f"2. '{NOTES_DIR}' folder se .md files read ho rahi hain...")
        md_loader = DirectoryLoader(
            NOTES_DIR, 
            glob="**/*.md", 
            loader_cls=TextLoader,
            loader_kwargs={"encoding": "utf-8"}
        )
        md_docs = md_loader.load()
        all_documents.extend(md_docs)
        print(f"   -> {len(md_docs)} Markdown notes load ho gaye.")
    else:
        print(f"'{NOTES_DIR}' folder nahi mila.")

    if not all_documents:
        print("❌ Koi data nahi mila! Notes ya trading_books folder check karein.")
        return

    print(f"\nTotal documents load huay: {len(all_documents)}")

    # 3. Text ko chunks mein split karein
    print("3. Text chunks banaye ja rahe hain...")
    text_splitter = RecursiveCharacterTextSplitter(
        chunk_size=1000,
        chunk_overlap=150
    )
    chunks = text_splitter.split_documents(all_documents)
    print(f"Total chunks bane: {len(chunks)}")

    # 4. Local embedding model load karein
    print("4. Embedding model load ho raha hai (all-MiniLM-L6-v2)...")
    embeddings = HuggingFaceEmbeddings(model_name="all-MiniLM-L6-v2")

    # 5. Chroma Database mein save karein
    print("5. Chroma DB mein save kiya ja raha hai...")
    vector_db = Chroma.from_documents(
        documents=chunks,
        embedding=embeddings,
        persist_directory=DB_DIR
    )
    print("✅ Knowledge Base kamyabi se save ho gaya (PDFs aur Notes dono shamil hain)!")

if __name__ == "__main__":
    build_vector_store()