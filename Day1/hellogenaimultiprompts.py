from openai import OpenAI
client=OpenAI()
prompts = [
    "Explain Generative AI in very simple terms — as if I’m 12 years old.",
    "Explain Generative AI in very simple terms — as if I’m 12 years old, and give a short real-world example kids can relate to.",
    # For system + user style, you can handle separately
]
model="gpt-4o-mini"
responses=[]
for i,prompt in enumerate(prompts):
    messages=[{"role":"user","content":prompt}]

    response = client.chat.completions.create(
        model=model,
        messages=messages
    )
    answer = response.choices[0].message.content
    responses.append(answer)
    print(f"\n🟢 Prompt {i+1}:\n{prompt}")
    print(f"💬 Response:\n{answer}")
    print("\n" + "-"*80)