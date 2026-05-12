from sqlalchemy import Column
from sqlalchemy import Integer
from sqlalchemy import String

from app.database import Base


class SecurityEvent(Base):

    __tablename__ = "security_events"

    id = Column(Integer, primary_key=True)

    source = Column(String)

    asset = Column(String)

    event_type = Column(String)

    severity = Column(String)

    risk_score = Column(Integer)

    threat_category = Column(String)

    recommended_action = Column(String)