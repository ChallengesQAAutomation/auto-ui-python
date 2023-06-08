import requests
import jsonschema

url = "https://jsonplaceholder.typicode.com/todos/1"

# Send GET request to the API
response = requests.get(url)

# Validate the success response
assert response.status_code == 200, "Test failed: Unexpected status code"

# Define the expected schema
expected_schema = {
    "type": "object",
    "properties": {
        "userId": {"type": "number"},
        "id": {"type": "number"},
        "title": {"type": "string"},
        "completed": {"type": "boolean"}
    },
    "required": ["userId", "id", "title", "completed"]
}

# Validate the response schema
try:
    jsonschema.validate(response.json(), expected_schema)
except jsonschema.exceptions.ValidationError as e:
    assert False, f"Test failed: Invalid response schema - {e}"

# If the code reaches this point, the test passed
print("Test passed: Success response and valid schema")
