# backend/api/improvement_tracking.py

from fastapi import APIRouter, HTTPException
from pydantic import BaseModel
from typing import List, Optional

# Router for improvement tracking
router = APIRouter()

# Example data model for improvement suggestions
class ImprovementSuggestion(BaseModel):
    suggestion_id: str
    description: str
    impact_score: float  # Higher scores indicate higher impact
    status: Optional[str] = "pending"  # Default status is "pending"

# Example in-memory data store
improvement_suggestions = []

@router.get("/", response_model=List[ImprovementSuggestion])
def get_all_suggestions():
    """
    Retrieve all improvement suggestions.
    """
    return improvement_suggestions

@router.get("/{suggestion_id}", response_model=ImprovementSuggestion)
def get_suggestion_by_id(suggestion_id: str):
    """
    Retrieve a specific improvement suggestion by its ID.
    """
    for suggestion in improvement_suggestions:
        if suggestion.suggestion_id == suggestion_id:
            return suggestion
    raise HTTPException(status_code=404, detail="Suggestion not found")

@router.post("/", response_model=ImprovementSuggestion)
def add_suggestion(suggestion: ImprovementSuggestion):
    """
    Add a new improvement suggestion.
    """
    for existing in improvement_suggestions:
        if existing.suggestion_id == suggestion.suggestion_id:
            raise HTTPException(status_code=400, detail="Suggestion ID already exists")
    improvement_suggestions.append(suggestion)
    return suggestion

@router.put("/{suggestion_id}", response_model=ImprovementSuggestion)
def update_suggestion(suggestion_id: str, updated_suggestion: ImprovementSuggestion):
    """
    Update an existing improvement suggestion by its ID.
    """
    for index, suggestion in enumerate(improvement_suggestions):
        if suggestion.suggestion_id == suggestion_id:
            improvement_suggestions[index] = updated_suggestion
            return updated_suggestion
    raise HTTPException(status_code=404, detail="Suggestion not found")

@router.delete("/{suggestion_id}")
def delete_suggestion(suggestion_id: str):
    """
    Delete an improvement suggestion by its ID.
    """
    for index, suggestion in enumerate(improvement_suggestions):
        if suggestion.suggestion_id == suggestion_id:
            del improvement_suggestions[index]
            return {"message": f"Suggestion {suggestion_id} deleted successfully"}
    raise HTTPException(status_code=404, detail="Suggestion not found")
# Placeholder content for backend/api/improvement_tracking.py
