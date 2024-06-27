from openai import OpenAI

client = OpenAI(
    api_key="45db4c851d9d41bf8ef190a881b129ab",
    base_url="https://api.aimlapi.com",
)


async def txt_bot(question):

    chat_completion = client.chat.completions.create(
        model="mistralai/Mistral-7B-Instruct-v0.2",
        messages=[
            {"role": "user", "content": question},
        ],
    )

    response = chat_completion.choices[0].message.content
    return (response)
