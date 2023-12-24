import openai

embedding = openai.Embedding.create(
    input="The cat is on the table",
    model="text-embedding-ada-002")["data"][0]["embedding"]
print(embedding)
print(embedding[1:10])
