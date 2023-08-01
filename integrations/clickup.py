import os

import requests
from dotenv import load_dotenv

from core.entities import ClickUpTask

load_dotenv()

CLICKUP_API_KEY = os.getenv("CLICKUP_TOKEN")
CLICKUP_API_URL = os.getenv("CLICKUP_API_URL")


def create_clickup_task(task: ClickUpTask):
    headers = {
        "Authorization": CLICKUP_API_KEY,
        "Content-Type": "application/json"
    }

    payload = {
        "name": task.email,
        "description": "New Task Description",
        "assignees": 183,
        "tags": "tag name 1",
        "status": "Open",
        "parent": None,
        "links_to": None,
        "custom_fields": task
    }

    response = requests.post(f"{CLICKUP_API_URL}/list/900200532843/task", headers=headers, json=payload)

    if response.status_code == 200:
        return response.json()
    else:
        return response.json()
