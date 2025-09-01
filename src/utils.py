import json
import os
import dotenv

dotenv.load_dotenv()
print(os.getenv('API_KEY'))
print(os.environ.get('API_KEY'))


def read_json_file(readfile):
    try:
        with open(readfile, encoding="utf-8") as f:
            text = f.read().replace("\n", "")
            operations = json.loads(text)
            return operations
    except (FileNotFoundError, json.JSONDecodeError):
        return []
