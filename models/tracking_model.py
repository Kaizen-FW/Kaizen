from sqlalchemy import Column, Integer, String, Float, DateTime, ForeignKey
from sqlalchemy.orm import relationship
from datetime import datetime
from . import Base  # Assuming Base is defined in a separate module for SQLAlchemy

class Tracking(Base):
    __tablename__ = 'tracking'

    id = Column(Integer, primary_key=True, autoincrement=True)
    user_id = Column(Integer, ForeignKey('users.id'), nullable=False)
    activity_type = Column(String, nullable=False)  # The type of activity (e.g., 'login', 'task_completion')
    activity_description = Column(String, nullable=True)  # Detailed description of the activity
    progress = Column(Float, default=0.0)  # Percentage of progress for the activity
    timestamp = Column(DateTime, default=datetime.utcnow)  # When the activity occurred
    is_completed = Column(Integer, default=0)  # A flag to mark whether the activity was completed

    # Relationship to the user model
    user = relationship("User", back_populates="trackings")
    
    def __init__(self, user_id, activity_type, activity_description=None, progress=0.0, is_completed=0):
        self.user_id = user_id
        self.activity_type = activity_type
        self.activity_description = activity_description
        self.progress = progress
        self.is_completed = is_completed

    def __repr__(self):
        return f"<Tracking(id={self.id}, user_id={self.user_id}, activity_type={self.activity_type}, progress={self.progress})>"

    def to_dict(self):
        return {
            "id": self.id,
            "user_id": self.user_id,
            "activity_type": self.activity_type,
            "activity_description": self.activity_description,
            "progress": self.progress,
            "timestamp": self.timestamp.isoformat(),
            "is_completed": self.is_completed
        }

    def update_progress(self, new_progress):
        """ Updates the progress of a specific activity. """
        self.progress = min(100.0, new_progress)  # Ensure progress doesn't exceed 100%
        self.is_completed = 1 if self.progress == 100 else 0
        self.timestamp = datetime.utcnow()

    def mark_as_completed(self):
        """ Marks the activity as completed (progress = 100). """
        self.progress = 100.0
        self.is_completed = 1
        self.timestamp = datetime.utcnow()
# Placeholder content for models/tracking_model.py
