import os
import openai
import json
import datetime
from dotenv import load_dotenv

load_dotenv()

# Set up the OpenAI API client
openai.api_key = os.getenv("OPENAI_API_KEY")


# Define a helper function to call the OpenAI API
def generate_code(promp, chat_tokens=[]):
    tokens = chat_tokens + [
        {"role": "system", "content": "You are an AI assistant that generates only code without any comments. You are given a prompt and you need to generate code that best completes the prompt without any additional markdown."},
        {"role": "user", "content": promp},
    ]

    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=tokens,
        n=1,
        stop=None,
        temperature=0.5,
    )



    # print(response)

    generated_code = response.choices[0].message.content.strip()
    chat_tokens.extend([{"role": "assistant", "content": generated_code}])
    return generated_code, chat_tokens


def execute_generated_code(generated_code):
    # Function to execute the generated code
    # IMPORTANT: Executing untrusted code can be risky; ensure you trust the generated code before running it
    exec(generated_code)


def save_to_file(prompt, generated_code, file_count):
    file_name = f"generated_code_{file_count}.txt"
    file_path = os.path.join('output', file_name)
    with open(file_path, "w") as f:
        f.write(f"Prompt:\n{prompt}\n\n")
        f.write(f"Generated Code:\n{generated_code}\n")
    print(f"Saved prompt and generated code to {file_name}")

# This helper function makes the datetime to a string so it can be appended to the file


def datetime_to_string():
    now = datetime.datetime.now()
    return now.strftime("%d%m%Y-%H%M%S")


# Initialize an empty list of tokens to maintain context
chat_tokens = []

time_now = datetime_to_string()
while True:
    # Get the prompt from the user
    prompt = input("Enter a prompt or 'exit' to quit: ").strip()
    if prompt.lower() == "exit":
        break

    # Generate code based on the prompt
    generated_code, chat_tokens = generate_code(prompt, chat_tokens)

    # Print the generated code
    print("Generated code:")
    print("----------------")
    print(generated_code)

    # Save the prompt and generated code to a file
    time_now = datetime_to_string()
    save_to_file(prompt, generated_code, time_now)

    # Ask for user approval
    # while True:
    #     user_input = input(
    #         "Do you want to run the generated code? (y/n): ").lower()
    #     if user_input == "y":
    #         # Execute the generated code
    #         execute_generated_code(generated_code)
    #         break
    #     elif user_input == "n":
    #         print("Skipping the execution of the generated code.")
    #         break
    #     else:
    #         print("Invalid input. Please enter 'y' or 'n'.")
    print("----------------")
    print("\n")

# Write a C# script for a scriptable object in Unity that is the base for a battle entity in a turn based rpg. Remember that each battle entity has stats (HP, MP, ATK, MAG, etc.) and a list of skills that can be used in battle. The script should be able to be attached to any game object in the scene and be able to be used as a base for any battle entity in the game.
