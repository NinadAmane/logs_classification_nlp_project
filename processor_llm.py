from dotenv import load_dotenv
from groq import Groq

load_dotenv()

groq = Groq()


def classify_with_llm(log_msg):
    prompt = f'''Classify the log message into one of these categories:
    (1) Workflow Error, (2) Deprecation Warning. 
    If you cant figure out a category, return "Unclassified".
    Only return the category name. No preamble.
    Log message: {log_msg}'''
    chat_completion = groq.chat.completions.create(
        messages=[
            {
                "role": "user",
                "content": prompt,
            }
        ],
        model="llama-3.3-70b-versatile",
    )

    response = chat_completion.choices[0].message.content.strip()
    return response


if __name__ == "__main__":
    print(classify_with_llm("API endpoint 'getCustomerDetails' is deprecate...	"))