from pydantic import BaseModel

from typing import List, Optional

class RequestSumBody(BaseModel):
    array: List[int]
    
class ResponseSum(BaseModel):
    sum: Optional[int] = None

class ResponseAsyncSum(BaseModel):
    session_id: str

