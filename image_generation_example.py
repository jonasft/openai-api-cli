import openai
import os

# Set up the OpenAI API client
openai.api_key = os.environ["OPENAI_API_KEY"]

def generate_image(prompt: str):
    # Call the ChatCompletion API
    
    try:
        response = openai.Image.create(
            prompt=prompt,
            n=1,
            size="1024x1024",
        )
        image_url = response['data'][0]['url']
        print(image_url)

    except Exception as e:
        print("exception")
        print(e)


if __name__ == "__main__":
    prompt = input("Enter the text prompt: ")
    print(f"\nRunning {os.path.basename(__file__)} with the prompt '{prompt}'...\n")
    generate_image(prompt)
