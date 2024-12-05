from fastapi import APIRouter

from . import message

main_router = APIRouter()
main_router.include_router(message.router)
