# https://zenn.dev/ml_bear/books/d1f060a3f166a5/viewer/0e8fe3
import tiktoken

encoding = tiktoken.encoding_for_model('gpt-3.5-turbo')
text = "This is a test for tiktoken."
tokens = encoding.encode(text)
print(len(text))  # 28
print(tokens)  # [2028, 374, 264, 1296, 369, 87272, 5963, 13]
print(len(tokens))  # 8

text = "今からtiktokenのトークンカウントテストを行います"
tokens = encoding.encode(text)
print(len(text))  # 28
print(tokens)  # [37271, 55031, 83, 1609, 5963, ...
print(len(tokens))  # 18
