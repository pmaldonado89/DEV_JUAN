from typing import Optional
from pydantic import BaseModel

class MinerSchema(BaseModel):
    id: Optional[int] = None
    full_name:str
    id_type:str
    id_number:str
    munucipality:str




