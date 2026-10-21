import json

def read_json(file_path: str) -> list[dict]:
    """Read JSON data from a file"""

    with open(file_path, "r") as file:
        data = json.load(file)
    return data

if __name__ == "__main__":
    result = read_json("data/input/function_calling_tests.json")
    for item in result:
        print(item["prompt"])
    result1 = read_json("data/input/functions_definition.json")
    for item in result1:
        print(item["name"], item["description"], item["parameters"])