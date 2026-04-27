from groq import Groq
import os
from dotenv import load_dotenv

load_dotenv()

client = Groq(api_key=os.getenv("GROQ_API_KEY"))


def summarize_text(text):
    try:
        response = client.chat.completions.create(
            model="llama-3.3-70b-versatile",
            messages=[
               {"role": "system", "content": "Summarize in 2-3 lines only"},
        {"role": "user", "content": text}
            ]
        )
        return response.choices[0].message.content

    except Exception as e:
        print("ERROR:", e)
        return "AI summary failed"    