from core.entities import HubSpotContact, ClickUpTask
from integrations import hubspot
from integrations.clickup import create_clickup_task


class ContactService:

    def create_hubspot_contact(self, contact: HubSpotContact):
        return hubspot.create_hubspot_contact(contact)

    def sync_contact_to_clickup(self, contact_id: int):
        contact = hubspot.get_hubspot_contact_by_id(contact_id)
        if contact:
            task = contact
            return create_clickup_task(task)
        else:
            return {"message": "Contact not found"}
