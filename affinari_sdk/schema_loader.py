import json
from pathlib import Path

def load_schema(path):
    with open(Path(path), 'r') as f:
        return json.load(f)