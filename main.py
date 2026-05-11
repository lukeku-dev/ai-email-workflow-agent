import os
from openai import OpenAI

client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

def classify_email(subject, content):
    prompt = f"""
    Classify the following email into one of these categories:
    important, promotion, receipt, newsletter, spam

    Subject: {subject}
    Content: {content}

    Only return the category.
    """

    response = client.chat.completions.create(
        model="gpt-4o-mini",
        messages=[{"role": "user", "content": prompt}],
    )

    return response.choices[0].message.content.strip()


if __name__ == "__main__":
    subject = "Your Amazon order receipt"
    content = "Thank you for your purchase..."

    category = classify_email(subject, content)
    print("Category:", category)
