import os
from dotenv import load_dotenv
from openai import AzureOpenAI
from json import JSONDecodeError, loads as j_loads
from json import load as __j_load


def import_json(file_name):
    with open(f"app/static/data/{file_name}.json", "r", encoding="utf-8") as f:
        return __j_load(f)
    
    
def file_to_str(file_name):
    with open(f"app/static/data/{file_name}", "r", encoding="utf-8") as f:
        return f.read()


class AI(AzureOpenAI):
    def __init__(self):
        AI_INSTRUCTIONS = file_to_str("AI_instructions.txt")
        BOT_OPTIONS = import_json("botOptions")
        PERSONALITY = import_json("personalities/fallen")

        load_dotenv(override=True)  # Load environment variables from .env file

        super().__init__(
            api_version="2024-12-01-preview",
            azure_endpoint=os.getenv("OPENAI_ENDPOINT"),
            api_key=os.getenv("OPENAI_API_KEY"),
        )

        self.prompt = [{"role": "system"}, {"role": "user"}]

        self.prompt[0]["content"] = AI_INSTRUCTIONS.replace("<botOptions>", str(BOT_OPTIONS)).replace(
            "<personality>", PERSONALITY["persona"]).replace("<name>", PERSONALITY["name"])

        self.flag_memory = True

    def __update_memory(self, msg, response):
        if self.flag_memory:
            self.flag_memory = False
            self.prompt[0]["content"] += "\nMEMORY:\n"
        self.prompt[0]["content"] += f"\nUser: {msg}\n\nAI: {response}\n"

    def callResponse(self, msg):
        self.prompt[1]["content"] = msg

        try:
            chat_response = self.chat.completions.create(
                messages=self.prompt,
                max_tokens=200,
                temperature=1.0,
                top_p=1.0,
                model="gpt-4o-mini",
            )
            chat_content = self.__str_to_json(
                chat_response.choices[0].message.content)
            self.__update_memory(msg, chat_content["response"])
            
        except:
            chat_content = {
                "response": "Something went wrong with the API, please reset the chat or report the issue!",
                "function": ["openIssue"]
            }

        return chat_content

    def __str_to_json(self, msg):
        try:
            # print(msg) # Debugging line to see the raw response
            response_json = j_loads(msg)
        except JSONDecodeError:
            response_json = {
                "response": "Congrats you broke the AI with your prompt, please reset the chat!",
                "function": ["error"]
            }
        return response_json

# # Example usage
# def test():
#     ai = AI()
#     while True:
#         user_input = input("You: ")
#         response = ai.callResponse(user_input)
#         print(f"AI: {response["response"]}")
#         print(f"Func: {response["function"]}")
# test()
