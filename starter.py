from llama_index import VectorStoreIndex, SimpleDirectoryReader
from dotenv import load_dotenv
load_dotenv()

document = SimpleDirectoryReader("data").load_data()
print()
print(type(document))
print(document)
document = SimpleDirectoryReader(
            input_files=["./omara.txt"]
        ).load_data()
print()
print(type(document))
print(document)
index = VectorStoreIndex.from_documents(document)
'''
index = VectorStoreIndex.from_documents(document)

query_engine = index.as_query_engine(streaming=True)
response = query_engine.query("In one sentence, explain what a JK Flip Flop is")
print(response)
'''