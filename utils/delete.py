import os
from typing import Any, List, Optional, Text, Dict

from rasa.nlu.config import RasaNLUModelConfig
from rasa.nlu.extractors import EntityExtractor
from rasa.nlu.model import Metadata
from rasa.nlu.training_data import Message

import json

match = {'dim': 'time', 'body': 'Nov 2', 'value': '{"values":[{"value":"2019-11-02T00:00:00.000+08:00","grain":"day","type":"value"},{"value":"2020-11-02T00:00:00.000+08:00","grain":"day","type":"value"},{"value":"2021-11-02T00:00:00.000+08:00","grain":"day","type":"value"}],"value":"2019-11-02T00:00:00.000+08:00","grain":"day","type":"value"}', 'start': 0, 'end': 5}

def extract_value(match):
    if match["value"].get("type") == "interval":
        value = {
            "to": match["value"].get("to", {}).get("value"),
            "from": match["value"].get("from", {}).get("value"),
        }
    else:
        value = match["value"].get("value")

    return value

x = match["value"]

d = json.loads(x)

print(d['value'])