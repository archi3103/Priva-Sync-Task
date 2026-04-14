from fastapi import APIRouter
import endpoint
import login

router = APIRouter()

router.include_router(endpoint.router, prefix="/events", tags=["events"])

router.include_router(login.router, tags=["auth"])