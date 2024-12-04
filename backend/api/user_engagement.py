# backend/api/user_engagement.py

from fastapi import APIRouter, HTTPException
from pydantic import BaseModel
from typing import List, Optional

# Router for user engagement
router = APIRouter()

# Example data model for user engagement
class UserEngagement(BaseModel):
    engagement_id: str
    user_id: str
    activity: str  # e.g., "completed_task", "joined_event", "earned_reward"
    timestamp: str  # ISO 8601 format: e.g., "2024-12-04T12:30:00Z"
    details: Optional[dict] = None  # Additional details about the engagement

# Example in-memory data store for user engagements
user_engagements = []

@router.get("/", response_model=List[UserEngagement])
def get_all_engagements():
    """
    Retrieve all user engagement records.
    """
    return user_engagements

@router.get("/{engagement_id}", response_model=UserEngagement)
def get_engagement_by_id(engagement_id: str):
    """
    Retrieve a specific user engagement record by its ID.
    """
    for engagement in user_engagements:
        if engagement.engagement_id == engagement_id:
            return engagement
    raise HTTPException(status_code=404, detail="Engagement not found")

@router.post("/", response_model=UserEngagement)
def create_user_engagement(engagement: UserEngagement):
    """
    Create a new user engagement record.
    """
    for existing_engagement in user_engagements:
        if existing_engagement.engagement_id == engagement.engagement_id:
            raise HTTPException(status_code=400, detail="Engagement ID already exists")
    user_engagements.append(engagement)
    return engagement

@router.put("/{engagement_id}", response_model=UserEngagement)
def update_user_engagement(engagement_id: str, updated_engagement: UserEngagement):
    """
    Update an existing user engagement record by its ID.
    """
    for index, engagement in enumerate(user_engagements):
        if engagement.engagement_id == engagement_id:
            user_engagements[index] = updated_engagement
            return updated_engagement
    raise HTTPException(status_code=404, detail="Engagement not found")

@router.delete("/{engagement_id}")
def delete_user_engagement(engagement_id: str):
    """
    Delete a user engagement record by its ID.
    """
    for index, engagement in enumerate(user_engagements):
        if engagement.engagement_id == engagement_id:
            del user_engagements[index]
            return {"message": f"Engagement {engagement_id} deleted successfully"}
    raise HTTPException(status_code=404, detail="Engagement not found")
# Placeholder content for backend/api/user_engagement.py
