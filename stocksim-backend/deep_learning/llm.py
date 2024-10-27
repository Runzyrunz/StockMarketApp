from transformers import pipeline

# Using the transformer package from HuggingFace, create an output string
# using the gpt2 model

# This will be used for the user to input text and have the LLM respond

llm = pipeline("text-generation", model="gpt2")

prompt = "What's the best way to invest in stocks?"
generated_text = llm(prompt, max_length=250, do_sample=True)

print(generated_text[0]['generated_text'])