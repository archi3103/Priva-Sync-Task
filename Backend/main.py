from fastapi import FastAPI
from router import router as main_hub
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()
app.include_router(main_hub)


app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

