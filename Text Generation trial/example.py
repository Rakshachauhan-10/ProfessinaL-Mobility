reader = SimpleDirectoryReader(
     input_files=["D:\Professional Mobility\Text Generation trial\course.txt"]
 )
docs = reader.load_data()
index = VectorStoreIndex.from_documents(docs)