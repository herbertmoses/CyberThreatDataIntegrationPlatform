from pydantic import BaseModel
from typing import Dict, Any

class LogData(BaseModel):
    source: str   # edr / cloud / cicd
    payload: Dict[str, Any]