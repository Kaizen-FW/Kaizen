# Placeholder content for models/evolution_model.pyfrom sqlalchemy import Column, Integer, String, Float, DateTime, ForeignKey
from sqlalchemy.orm import relationship
from datetime import datetime
from . import Base  # Assuming Base is defined in a separate module for SQLAlchemy

class Evolution(Base):
    __tablename__ = 'evolutions'

    id = Column(Integer, primary_key=True, autoincrement=True)
    user_id = Column(Integer, ForeignKey('users.id'), nullable=False)
    current_level = Column(Integer, default=1)  # User's current level in their evolution journey
    total_progress = Column(Float, default=0.0)  # Total progress in percentage (0 to 100)
    achievements = Column(String, nullable=True)  # List of achievements or milestones
    goal_description = Column(String, nullable=True)  # Describes the goal the user is working towards
    last_updated = Column(DateTime, default=datetime.utcnow)  # Timestamp when the model was last updated
    
    # Relationship to the user
    user = relationship("User", back_populates="evolutions")
    
    def __init__(self, user_id, current_level=1, total_progress=0.0, achievements=None, goal_description=None):
        self.user_id = user_id
        self.current_level = current_level
        self.total_progress = total_progress
        self.achievements = achievements if achievements else ""
        self.goal_description = goal_description

    def __repr__(self):
        return f"<Evolution(id={self.id}, user_id={self.user_id}, current_level={self.current_level}, total_progress={self.total_progress})>"

    def to_dict(self):
        return {
            "id": self.id,
            "user_id": self.user_id,
            "current_level": self.current_level,
            "total_progress": self.total_progress,
            "achievements": self.achievements,
            "goal_description": self.goal_description,
            "last_updated": self.last_updated.isoformat()
        }

    def update_progress(self, progress_increment):
        """ Update the total progress of the user based on completed tasks or milestones """
        self.total_progress = min(100.0, self.total_progress + progress_increment)
        self.last_updated = datetime.utcnow()

    def level_up(self):
        """ Update the user's level based on progress """
        if self.total_progress >= 100:
            self.current_level += 1
            self.total_progress = 0.0  # Reset progress after leveling up
        self.last_updated = datetime.utcnow()
