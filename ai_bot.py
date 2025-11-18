import openai

from openai import OpenAI

key = "key open ai"


client = OpenAI(api_key=key)

messages = [
    {"role": "system", "content": "You are a helpful assistant."}
]

def completion(message):
    messages.append({"role": "user", "content": message})

    try:
        response = client.chat.completions.create(
            model="gpt-4o-mini",
            messages=messages
        )
    except Exception as e:
        print("Error:", e)
        return None

    reply = response.choices[0].message.content
    messages.append({"role": "assistant", "content": reply})
    print("AI:", reply)
    return reply


if __name__ == "__main__":
    while True:
        user_question = input("You: ")
        if user_question.lower() in ["exit", "quit"]:
            break
        completion(user_question)
