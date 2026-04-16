from groq import Groq
from dotenv import load_dotenv
import os

load_dotenv()

def calling(prompt):
    client = Groq(
    api_key=os.environ.get("GROQ_API_KEY"),
    )

    chat_completion = client.chat.completions.create(
    messages=[
        {
            "role": "user",
            # "content": "Explain the importance of fast language models",
            "content": prompt,
        }
    ],
    model="openai/gpt-oss-20b",
    )

    return chat_completion.choices[0].message.content

# client = Groq(
#     api_key=os.environ.get("GROQ_API_KEY"),
# )

# chat_completion = client.chat.completions.create(
#     messages=[
#         {
#             "role": "user",
#             "content": "Explain the importance of fast language models",
#         }
#     ],
#     model="openai/gpt-oss-120b",
# )

# print(chat_completion.choices[0].message.content)

# output = calling()
# print(output)
