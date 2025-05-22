from langchain_community.document_loaders import DirectoryLoader

loader = DirectoryLoader(
  path = "foldername",
  glob = "*.pdf",
  loader_cls = PyPDFLoader
)

docs = loader.load()

print(docs[0].page_content)  # --> This will print the content of the document
