import openai

openai.api_key = "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"

def chatbot(prompt):
    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=[{"role": "user", "content": prompt}]
    )
    return response.choices[0].message['content'].strip()

def main():
    while True:
        prompt = input("Prompt: ")
        if prompt.lower() == "q":
            break
        print("Response: ", chatbot(prompt))

main()
