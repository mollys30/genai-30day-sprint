from openai import OpenAI

client = OpenAI()
model = "gpt-4o-mini"

# 1️⃣ Ask user for their prompt
user_prompt = input("Enter your prompt: ")

# 2️⃣ Ask user for a tone (funny, magical, serious)
tone = input("Choose a tone (funny/magical/serious): ")

# 3️⃣ Build messages array
messages = [
    # Add system role here that uses the tone dynamically
    {
        "role": "system", 
        "content": [
            {"type": "text", "text": f"You are a friendly teacher who explains things simply in a {tone} tone."}
            ]
    },
    # Add user role here
    {"role": "user", "content": [{"type": "text", "text": user_prompt}]}
]

# 4️⃣ Call the model
response = client.chat.completions.create(
    model=model,
    messages=messages
)

# 5️⃣ Print the assistant's reply
print(response.choices[0].message.content)
