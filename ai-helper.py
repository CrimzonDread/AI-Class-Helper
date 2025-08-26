import openai

# Replace 'your-api-key' with your actual OpenAI API key
openai.api_key = 'your-api-key'

def ask_ai(question):
    response = openai.ChatCompletion.create(
        model="gpt-4o-mini",  # or "gpt-4", "gpt-3.5-turbo" if available
        messages=[
            {"role": "system", "content": "You are a helpful assistant for class assignments."},
            {"role": "user", "content": question}
        ],
        max_tokens=500,
        temperature=0.7,
    )
    answer = response['choices'][0]['message']['content']
    return answer

def main():
    print("Welcome to your AI Class Assignment Helper!")
    while True:
        question = input("\nEnter your question (or type 'exit' to quit): ")
        if question.lower() == 'exit':
            print("Goodbye!")
            break
        answer = ask_ai(question)
        print("\nAI answer:\n", answer)

if __name__ == "__main__":
    main()
