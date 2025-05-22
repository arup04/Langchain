from langchain_community.document_loaders import WebBaseLoader

url = "url of the website"
loader =  WebBaseLoader(url)

# u can pass multiple urls as a list for using multiple website's content
docs = loader.load()

print(len(docs))
# gives 1 document per url