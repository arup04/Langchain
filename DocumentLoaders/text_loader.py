# all types of document Loaders are found in the Langchain_community module

from langchain_community.document_loaders import TextLoader

loader = TextLoader("cricket.txt",encoding="utf-8")

docs = loader.load()
# This will load the text file as a document into memory
# It will be a python List of Document objects

# print(docs)  --> print document

# print(type(docs))  --> list

# print(len(docs))  --> 1

# print(docs[0]) # --> Document with metadata

# print(type(docs[0])) # -->  <class 'langchain_core.documents.base.Document'>

# print(docs[0].page_content) # --> This will print the content of the document

# print(docs[0].metadata) # --> This will print the metadata of the document


