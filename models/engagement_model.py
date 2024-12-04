from sqlalchemy import Column, Integer, String, Float, DateTime, ForeignKey
from sqlalchemy.orm import relationship
from datetime import datetime
from . import Base  # Assuming Base is defined in a separate module for SQLAlchemy

class Engagement(Base):
    __tablename__ = 'engagements'

    id = Column(Integer, primary_key=True, autoincrement=True)
    user_id = Column(Integer, ForeignKey('users.id'), nullable=False)
    activity_type = Column(String, nullable=False)  # Type of activity (e.g., login, quest completion)
    activity_description = Column(String, nullable=True)  # Description of the activity
    engagement_score = Column(Float, default=0.0)  # Engagement score based on user interaction
    timestamp = Column(DateTime, default=datetime.utcnow)  # Timestamp of when the activity occurred
    
    # Relationship to the user
    user = relationship("User", back_populates="engagements")
    
    def __init__(self, user_id, activity_type, activity_description=None, engagement_score=0.0):
        self.user_id = user_id
        self.activity_type = activity_type
        self.activity_description = activity_description
        self.engagement_score = engagement_score

    def __repr__(self):
        return f"<Engagement(id={self.id}, user_id={self.user_id}, activity_type={self.activity_type}, engagement_score={self.engagement_score})>"

    def to_dict(self):
        return {
            "id": self.id,
            "user_id": self.user_id,
            "activity_type": self.activity_type,
            "activity_description": self.activity_description,
            "engagement_score": self.engagement_score,
            "timestamp": self.timestamp.isoformat()
        }

    def update_engagement_score(self, new_score):
        """ Update the engagement score based on some logic or activity completion """
        self.engagement_score = new_score
        # Additional logic can be implemented here to calculate score dynamically
# Placeholder content for models/engagement_model.py
