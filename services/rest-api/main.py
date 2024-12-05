from fastapi import FastAPI

from app.handlers import main_router
from app.gateways import rabbitmq

app = FastAPI()

app.include_router(main_router)


@app.on_event("shutdown")
async def graceful_shutdown():
    rabbitmq.connection.close()
