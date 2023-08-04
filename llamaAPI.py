import json
from llamaapi import LlamaAPI

llama = LlamaAPI("<your_api_token>")        #noch nicht erhalten

# API request
api_request_json = {
    "messages": [
        {"role": "user", "content": "Split this code:"+codeInput()+" into it's components and explain everyone of them in great detail."},
    ],
    "functions": [
        {
            "name": "explain_code",
            "description": "Explain the given code in great detail",
            "parameters": {
                "type": "object",
                "properties": {
                    "code": {
                        "type": "string",
                        "description": "Code written in a certain programming language"},
                },
            },
            "required": ["code"],
        }
    ],
    "stream": False,
    "function_call": "explain_code",
}

# Make your request and handle the response
response = llama.run(api_request_json)
print(json.dumps(response.json(), indent=2))