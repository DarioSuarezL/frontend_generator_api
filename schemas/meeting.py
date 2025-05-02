from pydantic import BaseModel
from typing import List
from uuid import UUID


class MeetingCreate(BaseModel):
    title: str


class MeetingResponse(BaseModel):
    id: UUID
    title: str
    design: str


class ListMeetingResponse(BaseModel):
    meetings: List[MeetingResponse]
