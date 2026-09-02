import tiktoken

enc= tiktoken.encoding_for_model("gpt-4o") #it means to create a token encoder for this model gpt-40 

text="Hey there! My name is Ishika"
tokens =enc.encode(text)

print("Tokens:",tokens)  #output:[25216, 1354, 0, 3673, 1308, 382, 83078, 3113]

#detokenization
decoded=enc.decode([25216, 1354, 0, 3673, 1308, 382, 83078, 3113])
print(decoded)