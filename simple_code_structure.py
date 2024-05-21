#Load all Libraries
import os
from dotenv import load_dotenv
import openai
import os.path
import sys
from llama_index.core.retrievers import VectorIndexRetriever
from llama_index.core.query_engine import RetrieverQueryEngine
from llama_index.core.indices.postprocessor import SimilarityPostprocessor
import os.path
from llama_index.core import (VectorStoreIndex,SimpleDirectoryReader,StorageContext,load_index_from_storage)
from llama_index.core import VectorStoreIndex,SimpleDirectoryReader,ServiceContext
from llama_index.core import Prompt
import pdb
from langchain_community.vectorstores import Chroma
from langchain.chains import RetrievalQA
from langchain_community.document_loaders import PyPDFLoader
from langchain_openai import OpenAIEmbeddings
from langchain_openai import ChatOpenAI
import warnings
warnings.filterwarnings("ignore", category=DeprecationWarning) 
from dotenv import load_dotenv, find_dotenv
_ = load_dotenv(find_dotenv())


#Checking the Keys for OpenAI Models
openai.api_key=os.getenv("OPENAI_API_KEY")

pdf_folder_path = "/home/mujeeb/LLM_Project/data"
for file in os.listdir(pdf_folder_path):
    if file.endswith('.pdf'):
        pdf_path = os.path.join(pdf_folder_path, file)
        loader = PyPDFLoader(pdf_path)
        docs=loader.load_and_split()


embeddings = OpenAIEmbeddings()
chroma_db = Chroma(persist_directory="data", embedding_function=embeddings,collection_name="market")
collection = chroma_db.get()

if len(collection['ids']) == 0:
    chroma_db = Chroma.from_documents(
        documents=docs,
        embedding=embeddings,
        persist_directory="data",
        collection_name="market"
        )

# Save the Chroma database to disk
chroma_db.persist()



if openai.api_key!=None:
    print("Open AI key is loaded from the Environment Now Loading Chroma DB")



def loading_and_storing_pdf():
    
    documents=SimpleDirectoryReader("data").load_data()
    index=VectorStoreIndex.from_documents(documents)

    query_engine=index.as_query_engine()
    retriever=VectorIndexRetriever(index=index,similarity_top_k=4)
    postprocessor=SimilarityPostprocessor(similarity_cutoff=0.80)
    query_engine=RetrieverQueryEngine(retriever=retriever,node_postprocessors=[postprocessor])

    # check if storage already exists
    PERSIST_DIR = "./storage"
    if not os.path.exists(PERSIST_DIR):
        # load the documents and create the index
        documents = SimpleDirectoryReader("data").load_data()
        index = VectorStoreIndex.from_documents(documents)
        # store it for later
        index.storage_context.persist(persist_dir=PERSIST_DIR)
    else:
        # load the existing index
        storage_context = StorageContext.from_defaults(persist_dir=PERSIST_DIR)
        index = load_index_from_storage(storage_context)
        return index


def ask_the_bot(question,index):
    template = (
        "We have provided context information below. \n"
        "---------------------\n"
        "{context_str}"
        "\n---------------------\n"
        "Given this information, please answer the question and each question should start with the word User: and each answer should start with code word Bot: {query_str}\n"
    )
    qa_template = Prompt(template)

    query_engine = index.as_query_engine(text_qa_template=qa_template)
    response = query_engine.query(question)
    print(response)



def ask_the_bot_vdb(question):
    llm = ChatOpenAI(model_name="gpt-3.5-turbo", temperature=0.8)
    chain = RetrievalQA.from_chain_type(llm=llm,chain_type="stuff",retriever=chroma_db.as_retriever())
    response = chain(question)
    print(response['result'])




index=loading_and_storing_pdf()


print("*********************************************************************************")
print("************Output from LLAMA with Local Storage & RAG***************************")
print("*********************************************************************************")

question="What are different types of marketplaces exist?"
ask_the_bot(question,index)


print("\n\n\n\n")
print("*********************************************************************************")
print("************Output from Chroma DB with OpenAI Embeddings*************************")
print("*********************************************************************************")



ask_the_bot_vdb(question)



