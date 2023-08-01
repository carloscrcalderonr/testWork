from pydantic import BaseModel

class HubSpotContact(BaseModel):
    company: str
    email: str
    firstname: str
    lastname: str
    phone: str
    website: str

class ClickUpTask(BaseModel):
    company: str
    email: str
    firstname: str
    lastname: str
    phone: str
    website: str
