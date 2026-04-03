from transformers import pipeline

chatbot = pipeline("text-generation", model="distilgpt2")

def ask_llm(prompt):
    response = chatbot(prompt, max_length=100, num_return_sequences=1)
    return response[0]['generated_text']

print("LLM Chatbot (type 'quit' to exit)")
while True:
    user_input = input("You: ")
    if user_input.lower() == "quit":
        break
    reply = ask_llm(user_input)
    print("LLM:", reply)
def get_llm_response(prompt: str) -> str:
    # If your LLM instance is called 'llm'
    return llm(prompt)
