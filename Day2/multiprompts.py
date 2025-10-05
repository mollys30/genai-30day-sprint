from openai import OpenAI
client=OpenAI()
responses=[]
prompts=["What is Generative AI in simple words?",
    "Give me 3 real-life applications of Generative AI.",
    "What is the difference between Generative AI and Traditional AI?"]
model="gpt-4o-mini"
for i,text in enumerate(prompts,start=1):
        response=client.chat.completions.create(model=model,messages=[{"role":"user","content": [{"type": "text", "text": text}]}])
        answer=response.choices[0].message.content
        responses.append(f"🟢 Prompt {i}: {text}\n💬 Response:\n{answer}\n{'-'*80}\n")

with open("Day2_responses.txt", "w", encoding="utf-8") as f:
    f.writelines(responses)

print("✅ All prompts completed and saved to Day2_responses.txt")


