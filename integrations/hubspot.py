import os

import requests
from dotenv import load_dotenv

from core.entities import HubSpotContact
load_dotenv()

HUBSPOT_API_KEY = os.getenv("HUBSPOT_ACCESS_TOKEN")
HUBSPOT_API_URL = os.getenv("HUBSPOT_API_URL")


def create_hubspot_contact(contact: HubSpotContact):
    headers = {
        "Authorization": f"Bearer {HUBSPOT_API_KEY}",
        "Content-Type": "application/json"
    }

    payload = {
        "properties": {
            "email": contact.email,
            "firstname": contact.firstname,
            "lastname": contact.lastname,
            "phone": contact.phone,
            "website": contact.website,
            "company": contact.company,
        }
    }

    response = requests.post(HUBSPOT_API_URL, headers=headers, json=payload)
    if response.status_code == 200:
        return response.json()
    else:
        return response.json()


def get_hubspot_contact_by_id(contact_id: str):
    headers = {
        "Authorization": f"Bearer {HUBSPOT_API_KEY}",
        "Content-Type": "application/json"
    }

    params = {
        "archived": "false"
    }

    response = requests.get(f"{HUBSPOT_API_URL}/{contact_id}", headers=headers, params=params)
    if response.status_code == 200:
        return response.json()
    else:
        return response.json()["message"]
