# Main FastAPI app
from fastapi import FastAPI, HTTPException, Request
from fastapi.responses import JSONResponse
from fastapi.middleware.cors import CORSMiddleware
from fastapi.routing import APIRouter
from pydantic import BaseModel
from typing import List

# Create FastAPI app instance
app = FastAPI(
    title="Kaizen Agent Framework API",
    description="An API to manage user engagement, improvement tracking, and self-evolution logic.",
    version="1.0.0"
)

# Middleware for Cross-Origin Resource Sharing (CORS)
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Adjust this for better security in production
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Example data models
class UserEngagement(BaseModel):
    user_id: str
    activity: str
    timestamp: str

class ImprovementSuggestion(BaseModel):
    suggestion_id: str
    description: str
    impact_score: float

# Example in-memory database
user_engagements = []
improvement_suggestions = []

# Routers
router = APIRouter()

@router.get("/", tags=["General"])
def read_root():
    """
    Root endpoint providing a welcome message.
    """
    return {"message": "Welcome to the Kaizen Agent Framework API!"}

@router.post("/engagements", response_model=UserEngagement, tags=["User Engagement"])
def add_user_engagement(engagement: UserEngagement):
    """
    Add a new user engagement record.
    """
    user_engagements.append(engagement)
    return engagement

@router.get("/engagements", response_model=List[UserEngagement], tags=["User Engagement"])
def list_user_engagements():
    """
    Retrieve all user engagement records.
    """
    return user_engagements

@router.post("/improvements", response_model=ImprovementSuggestion, tags=["Improvement Suggestions"])
def add_improvement_suggestion(suggestion: ImprovementSuggestion):
    """
    Add a new improvement suggestion.
    """
    improvement_suggestions.append(suggestion)
    return suggestion

@router.get("/improvements", response_model=List[ImprovementSuggestion], tags=["Improvement Suggestions"])
def list_improvement_suggestions():
    """
    Retrieve all improvement suggestions.
    """
    return improvement_suggestions

# Global exception handler for 404 errors
@app.exception_handler(404)
def not_found_handler(request: Request, exc: HTTPException):
    return JSONResponse(
        status_code=404,
        content={"message": "Resource not found. Please check the URL or endpoint."}
    )

# Include router in the application
app.include_router(router)
