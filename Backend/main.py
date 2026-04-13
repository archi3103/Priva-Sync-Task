from fastapi import FastAPI
from router import router as process_router
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()
app.include_router(process_router)


app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

