from ollama import Client

client = Client(host="https://8e6c-34-16-198-44.ngrok-free.app")

try:
    output = client.generate(
        model="llama3",
        prompt="Once upon a time",
        stream=False,
    )
    print(output['response'])   
except Exception as e:
    print(f"Error: {e}")

