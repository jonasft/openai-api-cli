import openai
import os
import argparse

# Set up the OpenAI API client
openai.api_key = os.environ["OPENAI_API_KEY"]

def generate_text(prompt):
    # Call the Completion API
    response = openai.Completion.create(
        engine="text-davinci-002",
        prompt=prompt,
        max_tokens=50,
        n=1,
        stop=None,
        temperature=0.7,
    )

    # Extract and print the generated text
    generated_text = response.choices[0].text.strip()
    print(f"Generated text: {generated_text}")

if __name__ == "__main__":

    prompt = input("Enter the text prompt: ")
    print(f"Running {os.path.basename(__file__)} with the prompt '{prompt}'...")

    generate_text(prompt)
