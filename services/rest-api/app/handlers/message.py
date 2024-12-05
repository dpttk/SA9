from fastapi import APIRouter, HTTPException

from app.domain.message import Message
from app.gateways.rabbitmq import send_to_queue

router = APIRouter(prefix="/message")


@router.post("/")
async def send_message(msg: Message):
    try:
        send_to_queue(str(msg))
        return {"status": "Message sent"}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
