from fastapi import APIRouter, Depends
from helpers.auth import get_current_user
from models.user import User
from models.meeting import Meeting
from schemas.meeting import MeetingCreate, MeetingResponse, ListMeetingResponse

router = APIRouter()


@router.post("/create", response_model=MeetingResponse)
async def create_meeting(
    meeting_data: MeetingCreate, current_user: User = Depends(get_current_user)
):
    meeting = await Meeting.create(title=meeting_data.title, owner=current_user)

    return {"id": meeting.id, "title": meeting.title, "design": meeting.design}


@router.get("/list", response_model=ListMeetingResponse)
async def list_meeting(current_user: User = Depends(get_current_user)):
    meetings = await current_user.owned_meetings
    return {"meetings": meetings}
