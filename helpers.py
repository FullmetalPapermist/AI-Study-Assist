import json
import re
import subprocess

def clear_console():
    subprocess.run("cls", shell=True)


def compute_timeout(text):
    num_tokens = len(text) // 4
    tokens_per_seconds = 30
    base = 10
    return base + (num_tokens / tokens_per_seconds)

def parse_response(response):
    text = str(response)

    try:
        # extract JSON block
        json_match = re.search(r"\{[\s\S]*?\}", text)
        if json_match:
            return json.loads(json_match.group())
        else:
            raise ValueError("No JSON found")

    except Exception as e:
        print("Raw response:", text)
        raise ValueError("Failed to parse JSON") from e