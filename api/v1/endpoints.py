from fastapi import APIRouter, BackgroundTasks, Depends
from services.contact_service import ContactService
from core.entities import HubSpotContact
from services.logger import AppLogger

router = APIRouter()
app_logger = AppLogger()


@router.post("/hubspot/contact/")
async def create_hubspot_contact(
        contact: HubSpotContact,
        contact_service: ContactService = Depends(ContactService)
):
    app_logger.log_request("POST", "/hubspot/contact/", contact.dict())
    response = contact_service.create_hubspot_contact(contact)
    app_logger.log_response(response)
    return response


@router.get("/contact/{contact_id}/sync/")
async def sync_contact_to_clickup(
        contact_id: int,
        background_tasks: BackgroundTasks,
        contact_service: ContactService = Depends(ContactService)
):
    app_logger.log_request("GET", f"/contact/{contact_id}/sync/")
    background_tasks.add_task(contact_service.sync_contact_to_clickup, contact_id)

    return {"message": "Syncing contact with ClickUp in the background."}
