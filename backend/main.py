from fastapi import FastAPI
from fastapi import Request
import time
from routers.chat_router import router as chat_r
app = FastAPI()
app.include_router(chat_r)
