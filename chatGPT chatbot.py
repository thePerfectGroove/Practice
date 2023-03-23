import openai
import prompt_toolkit

# set up the OpenAI API credentials
openai.api_key = "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"

# define a function to generate a response using the ChatGPT API
def generate_response(prompt):
    response = openai.Completion.create(
        engine="text-davinci-002",
        prompt=prompt,
        temperature=0.7,
        max_tokens=1024,
        top_p=1,
        frequency_penalty=2,
        presence_penalty=2
    )
    return response.choices[0].text.strip()

# set up the chat loop
while True:
    # prompt the user for input
    user_input = prompt_toolkit.prompt("> ")
    
    # generate a response to the user input
    response = generate_response(user_input)
    
    # print the response
    print(response)
