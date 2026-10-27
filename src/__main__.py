import json
from typing import Literal
from pydantic import BaseModel


class ParameterDefinition(BaseModel):
    type: Literal["string", "number"]


class FunctionDefinition(BaseModel):
    name: str
    description: str
    parameters: dict[str, ParameterDefinition]


class TestCase(BaseModel):
    prompt: str


def read_json(file_path: str) -> list[dict]:
    """Read JSON data from a file"""

    with open(file_path, "r") as file:
        data = json.load(file)
    return data



if __name__ == "__main__":
    result = read_json("data/input/function_calling_tests.json")


    for item in result:
        test = TestCase.model_validate(item)
        prompt = test.prompt
        print(test.prompt)

    result1 = read_json("data/input/functions_definition.json")
    functions_list = []

    for item in result1:
        function = FunctionDefinition.model_validate(item)
        functions_list.append(function)

    selected_function = None
    for function in functions_list:
        print(function.name)
        if function.name == "fn_reverse_string":
            selected_function = function
    if selected_function is not None:
        print(function.name, function.description, function.parameters)

        for param_name, param_info in function.parameters.items():
            print(param_name, param_info.type)

    print(len(functions_list))
    print(functions_list[0].parameters["a"].type)    
    print(functions_list[1].parameters["name"].type)    

    print(functions_list[2].description)    

    prompt_text = "Choose the most appropriate function for the user's request and return its parameters as JSON.\n"

    prompt_text += f"\nUser request: {result[0]['prompt']}\n"

    for function in functions_list:
        prompt_text += f"{function.name}: {function.description}\n"

        for param_name, param_info in function.parameters.items():
            prompt_text += f"{param_name}: {param_info.type}\n"
    
    print(prompt_text)

