"""
JSON helper functions.
"""

import json


def parse_json(text: str):

    try:
        return json.loads(text)

    except Exception:

        return None