from openai import OpenAI

# Pass the API key directly (quick and works immediately)
client = OpenAI(api_key="sk-your_actual_key_here")

prompt = "Explain Generative AI in very simple terms — as if I’m 12 years old."
messages = [{"role": "user", "content": prompt}]
model = "gpt-4o-mini"

# Call the model
response = client.chat.completions.create(model=model, messages=messages)

# Print the AI's reply
print(response.choices[0].message.content)
