from langchain_community.document_loaders import PyPDFLoader

# first pip install PyPDF
loader = PyPDFLoader("cricket.pdf")
docs = loader.load()

print(docs)  # --> print document
print(type(docs))  # --> list 
print(len(docs))  # --> 23 if pdf contains 23 pages
