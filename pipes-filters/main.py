from multiprocessing import Process, Queue

from fastapi import FastAPI, HTTPException
import uvicorn

from app import filters
from app.domain.message import Message

input_queue = Queue()
filtered_queue = Queue()
output_queue = Queue()

api = FastAPI()


@api.post("/message/")
async def send_message(msg: Message):
    try:
        input_queue.put(msg)
        return {"status": "Message sent"}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


filter_filter = filters.FilterFilter(input_queue, filtered_queue)
screaming_filter = filters.ScreamingFilter(filtered_queue, output_queue)
publisher_filter = filters.PublisherFilter(output_queue, None)

filter_process = Process(target=filter_filter.process)
screaming_process = Process(target=screaming_filter.process)
publisher_process = Process(target=publisher_filter.process)

api_process = Process(target=uvicorn.run, args=(api,), kwargs={"host": "0.0.0.0", "port": 8000})
api_process.start()

filter_process.start()
screaming_process.start()
publisher_process.start()

filter_process.join()
screaming_process.join()
publisher_process.join()
api_process.terminate()
