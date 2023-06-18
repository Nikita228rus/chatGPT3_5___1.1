import openai
import textwrap


def chat_bot():

    openai.api_key = ("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")
    model_engine = "gpt-3.5-turbo"
    max_tokens = 1024

    s = '```'
    prompt = [
       {"role": "system", "content": "You are a helpful assistant."}
    ]

    while True:
        content = input("User: ")
        prompt.append({"role": "user", "content": content})
        completion = openai.ChatCompletion.create(
            model=model_engine,
            max_tokens=max_tokens,
            messages=prompt,
            temperature=0.5
        )

        chat_response = completion.choices[0].message.content
        text_wrap = textwrap.wrap(chat_response, width=150)

        for i in text_wrap:
            print(i)
        #print(chat_response)

        prompt.append({"role": "assistant", "content": chat_response})



chat_bot()