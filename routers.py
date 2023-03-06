import asyncio
from uuid import uuid4

from fastapi import HTTPException

from typing import List, Dict

from app import app, sessions
from serializers import (RequestSumBody,
                         ResponseSum,
                         ResponseAsyncSum)

@app.post("/api/sync_sum", response_model=ResponseSum)
def sync_sum(body: RequestSumBody):
    sm = sum(body.array)
    
    return ResponseSum(sum=sm)

@app.post("/api/async_sum", response_model=ResponseAsyncSum)
async def async_sum(body: RequestSumBody):
    session_id = str(uuid4())
    sessions.update({session_id: None})
    
    asyncio.create_task(sum_task(session_id, body.array))

    return ResponseAsyncSum(session_id=session_id)
    
async def sum_task(session_id: int, num_list: List[int]):
    res = sum(num_list)
    sessions[session_id] = res
    
@app.get("/api/async_sum/{session_id}", response_model=ResponseSum)
async def get_async_sum(session_id: str, timeout: int = 10):
    if session_id not in sessions:
        raise HTTPException(status_code=404, detail="No session found")
    
    try:
        res = await asyncio.wait_for(get_session_result(session_id), timeout=timeout)
        return ResponseSum(sum=res)
    
    except asyncio.TimeoutError:
        return ResponseSum(sum=None)
    
async def get_session_result(session_id: str):
    while True:
        res = sessions.get(session_id)
        
        if res:
            return res
        
        await asyncio.sleep(1)
        
    