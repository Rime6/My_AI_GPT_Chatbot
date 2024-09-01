import openai

openai.api_key = "my_secret_key_code_that_I_will_not_be_sharing_with_you_lol"

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
