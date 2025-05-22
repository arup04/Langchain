from langchain_community.document_loaders import CSVLoader

loader = CSVLoader(
    file_path="cricket.csv"
)

data = loader.load()
print(len(data)) # -- gives number of rows in the csv file
print(data[0])

# this loader works in such a way that it creates a document for each row in the csv file
# so if the csv file has 10 rows, it will create 10 documents
