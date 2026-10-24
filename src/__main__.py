import json
from pydantic import BaseModel

def read_json(file_path: str) -> list[dict]:
    """Read JSON data from a file"""

    with open(file_path, "r") as file:
        data = json.load(file)
    return data
class ParameterDefinition(BaseModel):
    type: str

class FunctionDefinition(BaseModel):
    name: str
    description: str
    parameters: dict[str, ParameterDefinition]


if __name__ == "__main__":
    result = read_json("data/input/function_calling_tests.json")
    for item in result:
        print(item["prompt"])
    result1 = read_json("data/input/functions_definition.json")
    for item in result1:
        function = FunctionDefinition.model_validate(item)
        print(function)
        print(function.name, function.description, function.parameters)
        for param_name, param_info in function.parameters.items():
            print(param_name, param_info)
            print(param_info["type"])
    
