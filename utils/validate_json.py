import json
import jsonschema
from jsonschema import validate


def get_schema():
    """This function loads the given schema available"""
    with open('user_schema.json', 'r') as file:
        schema = json.load(file)
    return schema


def validate_json(instance, schema):
    """REF: https://json-schema.org/ """
    # Describe what kind of json you expect.
    # execute_api_schema = get_schema()

    try:
        validate(instance=instance, schema=schema)
    except jsonschema.exceptions.ValidationError as err:
        print(err)
        err = "Given JSON data is InValid"
        return False

    message = "Given JSON data is Valid"
    return True
