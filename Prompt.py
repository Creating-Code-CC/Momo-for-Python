import openai
import requests
import os
class Prompt:
    def prompt_model(self, default):
        openai.api_key = "sk-key"
        response= openai.Completion.create(
        model="text-davinci-002",
        prompt="Give me 10 unordered items for " + default,
        max_tokens=50,
        temperature=0,
        echo=True
        )
        response = response["choices"]
        response = response[0]
        response = response["text"]
        response = response.partition(default)
        response = response[2]
        if '1' in response:
            for x in range(1,11):
                response = response.replace(str(x)+'.' , '-')
        return response.split('-')